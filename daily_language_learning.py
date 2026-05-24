import os
import json
import random
import datetime
import asyncio
import tempfile
import edge_tts
from docx import Document
from google import genai
from google.genai import types

# ==========================================
# ⚙️ 설정
# ==========================================
# GitHub Actions에서는 환경변수로 전달, 로컬에서는 직접 입력
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# GitHub Actions 환경 여부 감지
IS_GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"

# 1. 언어별 설정
LANGUAGES = [
    {
        "name": "영어",
        "folder": "영어",
        # 듀엣 대화 효과를 위한 여성, 남성 성우진 지정
        "voices": ["en-US-JennyNeural", "en-US-GuyNeural"], 
        "rate": "+0%",                
        "prompt_extra": "미국식 영어 기준으로 번역 및 작성하며, Chunking(끊어 읽기 표기)은 절대 생략하고 자연스러운 원문과 해석만 제공하세요."
    },
    {
        "name": "중국어",
        "folder": "중국어",
        # 듀엣 대화 효과를 위한 여성, 남성 성우진 지정
        "voices": ["zh-CN-XiaoxiaoNeural", "zh-CN-YunxiNeural"], 
        "rate": "-10%",                  
        "prompt_extra": "중국어 간체자로 번역 및 작성하며, 모든 중국어 원문과 단어에는 반드시 발음 기호인 병음(Pinyin)을 함께 표기하세요. (Chunking 생략)"
    }
]

STYLES = [
    "일상적인 대화 (Casual Small Talk, Daily Conversation)",
    "업무 비즈니스 회화 (Business Meeting, Networking, Collaboration)",
    "직장 내 캐주얼한 소통 (Workplace Casual Talk, Coffee Chat)"
]
TOPICS = [
    "일상 생활 (취미, 여행, 쇼핑, 외식, 건강)",
    "회사 업무 및 협업 (프로젝트 진행, 동료와의 협력, 일정 조율)",
    "비즈니스 네트워킹 (아이스브레이킹, 스몰토크, 첫 만남)",
    "의견 교환 및 문제 해결 (설득, 조율, 피드백 주고받기)",
    "자기계발 및 커리어 (생산성 향상, 목표 설정, 커리어 고민)"
]

# ==========================================
# 📂 Google Drive 업로드 기능 (GitHub Actions 전용)
# ==========================================
def get_drive_service():
    """Google Drive API 서비스 객체 생성 (OAuth 2.0 사용자 인증)"""
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    
    creds_json = os.environ.get("GOOGLE_USER_CREDENTIALS")
    if not creds_json:
        print("⚠️ GOOGLE_USER_CREDENTIALS 환경변수가 없습니다. 업로드를 건너뜁니다.")
        return None
    
    creds_info = json.loads(creds_json)
    credentials = Credentials.from_authorized_user_info(
        creds_info, scopes=["https://www.googleapis.com/auth/drive"]
    )
    
    # 만약 토큰이 만료되었다면 갱신
    if credentials.expired and credentials.refresh_token:
        try:
            credentials.refresh(Request())
        except Exception as e:
            print(f"⚠️ 토큰 갱신 중 오류 발생: {e}")
            
    return build("drive", "v3", credentials=credentials)

def find_or_create_folder(service, folder_name, parent_id=None):
    """Google Drive에서 폴더를 찾거나, 없으면 새로 생성"""
    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    
    results = service.files().list(q=query, spaces="drive", fields="files(id, name)").execute()
    files = results.get("files", [])
    
    if files:
        return files[0]["id"]
    
    # 폴더가 없으면 새로 생성
    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
    }
    if parent_id:
        file_metadata["parents"] = [parent_id]
    
    folder = service.files().create(body=file_metadata, fields="id").execute()
    print(f"📁 Google Drive 폴더 생성: {folder_name}")
    return folder.get("id")

def upload_to_drive(service, local_path, folder_id, filename):
    """파일을 Google Drive 특정 폴더에 업로드"""
    from googleapiclient.http import MediaFileUpload
    
    # 같은 이름의 파일이 이미 있으면 업데이트
    query = f"name='{filename}' and '{folder_id}' in parents and trashed=false"
    results = service.files().list(q=query, spaces="drive", fields="files(id)").execute()
    existing = results.get("files", [])
    
    media = MediaFileUpload(local_path, resumable=True)
    
    if existing:
        # 기존 파일 업데이트
        service.files().update(fileId=existing[0]["id"], media_body=media).execute()
    else:
        # 새 파일 생성
        file_metadata = {"name": filename, "parents": [folder_id]}
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    
    print(f"   ☁️ Google Drive 업로드 완료: {filename}")

def upload_folder_to_drive(service, local_folder, today_folder_name):
    """로컬 출력 폴더의 모든 파일을 Google Drive에 업로드"""
    # [언어 공부] 폴더 명시적 ID (사용자 제공)
    parent_id = "1YmABh3RfKVsqrAVWFelKn2NCtY9ezrCS"
    
    # 오늘 날짜 폴더 찾기/생성
    date_folder_id = find_or_create_folder(service, today_folder_name, parent_id)
    
    # 폴더 안의 모든 파일 업로드
    for filename in os.listdir(local_folder):
        filepath = os.path.join(local_folder, filename)
        if os.path.isfile(filepath):
            upload_to_drive(service, filepath, date_folder_id, filename)


# ==========================================
# 📄 문서 생성
# ==========================================
def create_docx(data, filename, lang_name, style, topic):
    doc = Document()
    
    # 제목
    doc.add_heading(f'🧠 오늘의 {lang_name} 훈련 ({topic} - {style})', 0)
    
    # 배경지식
    doc.add_heading('배경지식', level=1)
    doc.add_paragraph(data.get('background_kr', ''))
    
    # 훈련 문장
    doc.add_heading('🎧 청취 훈련 문장', level=1)
    for i, s in enumerate(data.get('sentences', []), 1):
        p = doc.add_paragraph()
        p.add_run(f"{i}. {s.get('original', '')}\n").bold = True
        
        # 병음이 있다면 추가 (중국어용)
        if s.get('pinyin'):
            p.add_run(f"   [{s.get('pinyin')}]\n")
            
        p.add_run(f"   해석: {s.get('translation', '')}")

    # 핵심 단어
    doc.add_heading('📝 핵심 단어', level=1)
    for i, v in enumerate(data.get('vocabulary', []), 1):
        p = doc.add_paragraph()
        word_text = f"{i}. {v.get('word', '')}"
        if v.get('pinyin'):
            word_text += f" [{v.get('pinyin')}]"
        word_text += f" - {v.get('pos', '')} {v.get('meaning', '')}"
        p.add_run(word_text)

    # 덩어리 표현
    doc.add_heading('🧩 핵심 표현 (Collocations/Idioms)', level=1)
    for i, c in enumerate(data.get('collocations', []), 1):
        p = doc.add_paragraph()
        exp_text = f"{i}. {c.get('expression', '')}"
        if c.get('pinyin'):
            exp_text += f" [{c.get('pinyin')}]"
        exp_text += f" - {c.get('meaning', '')}"
        p.add_run(exp_text)

    doc.save(filename)


# ==========================================
# 🎵 메인 실행
# ==========================================
async def main_async():
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    # KST(한국 시간) 기준 날짜 계산 (UTC+9)
    import pytz
    kst = pytz.timezone("Asia/Seoul")
    now = datetime.datetime.now(kst)
    weekdays = ["월", "화", "수", "목", "금", "토", "일"]
    weekday_str = weekdays[now.weekday()]
    today_folder_name = f"{now.strftime('%Y%m%d')} ({weekday_str})"
    
    # 출력 폴더 결정
    if IS_GITHUB_ACTIONS:
        # GitHub Actions: 임시 로컬 폴더에 생성 후 Google Drive에 업로드
        base_dir = os.path.join(os.getcwd(), "output")
    else:
        # 로컬 실행: 기존과 동일하게 스크립트 위치 기준
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    target_folder = os.path.join(base_dir, today_folder_name)
    os.makedirs(target_folder, exist_ok=True)

    selected_style = random.choice(STYLES)
    selected_topic = random.choice(TOPICS)

    print(f"\n🔄 [다국어 자동화 파이프라인 시작]")
    print(f"👉 오늘의 주제: {selected_topic} / 스타일: {selected_style}")
    if IS_GITHUB_ACTIONS:
        print(f"☁️ GitHub Actions 클라우드 실행 모드")

    # --- 공통 한국어 스크립트 생성 ---
    print("⏳ 동일한 학습 내용을 위해 공통 한국어 스크립트를 먼저 생성합니다...")
    master_prompt = f"""
    당신은 제2외국어 학습을 위한 실전 회화 작성 전문가입니다.
    실제 원어민들이 일상생활과 직장 업무 환경에서 자연스럽게 주고받는 생생한 대화나 스크립트를 하나 창작해주세요.
    
    [설정]
    - 스타일: {selected_style}
    - 주제: {selected_topic}
    - 분량: 가장 핵심이 되는 실전 대화 문장 5개로 구성
    
    [작성 규칙]
    - 교과서적인 딱딱한 표현 대신, 실제 대화나 구어체(Colloquial)에서 즉시 활용할 수 있는 유용하고 살아있는 표현(구동사, 관용구, 직장인 실무 구어 등)을 자연스럽게 포함해주세요.
    
    이 스크립트는 향후 여러 언어(영어, 중국어 등)로 번역되어 동일한 내용의 실전 회화 자료로 쓰일 예정입니다.
    응답은 반드시 아래 JSON 형식으로만 작성해주세요.
    {{
      "background_kr": "상황 설명 (한글로 2~3문장)",
      "korean_sentences": [
        "1번째 문장", "2번째 문장", "3번째 문장", "4번째 문장", "5번째 문장"
      ]
    }}
    """
    
    master_data = None
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=master_prompt,
                config=types.GenerateContentConfig(response_mime_type="application/json")
            )
            resp_text = response.text.strip()
            if resp_text.startswith("```json"):
                resp_text = resp_text[7:]
            if resp_text.endswith("```"):
                resp_text = resp_text[:-3]
            master_data = json.loads(resp_text.strip())
            break
        except Exception as e:
            print(f"⚠️ 공통 스크립트 생성 실패 ({attempt+1}/3): {e}")
            await asyncio.sleep(10)
            
    if not master_data:
        print("❌ 공통 스크립트 생성에 실패하여 작업을 종료합니다.")
        return

    print("✅ 공통 스크립트 생성 완료!")
    # API 요청 제한 완화를 위해 5초 대기
    await asyncio.sleep(5)

    for lang in LANGUAGES:
        print(f"\n=========================================")
        print(f"▶️ [{lang['name']}] 학습 자료 생성 시작...")
        
        prompt = f"""
        당신은 자율형 AI 학습 자동화 에이전트이자 제2외국어 습득에 특화된 데이터 엔지니어입니다.
        오늘 생성할 언어는 '{lang['name']}'입니다.
        
        아래의 [공통 한국어 스크립트]를 바탕으로 '{lang['name']}' 실전 회화 학습 자료를 생성하세요.
        내용과 의미가 원본 한국어 스크립트와 완전히 일치하되, 번역 시에는 '{lang['name']}' 모국어 사용자들이 실제 일상생활과 직장에서 매일 쓰는 가장 자연스럽고 생생한 구어체 표현(Colloquial/Casual/Natural Business)을 적극적으로 사용해야 합니다. 
        직역해서 어색해지는 교과서식 영어나 중국어 문장은 피해주세요.

        [공통 한국어 스크립트]
        - 배경지식: {master_data.get('background_kr')}
        - 한국어 문장 5개: {master_data.get('korean_sentences')}

        - 추가 요구사항: {lang['prompt_extra']}

        (절대로 Chunking(의미 단위 끊어 읽기 표기)은 하지 마세요!)

        반드시 아래의 JSON 형식으로만 응답하세요.

        {{
          "background_kr": "상황 설명 (제공된 배경지식과 동일하게 유지)",
          "sentences": [
            {{
              "original": "제공된 한국어 문장을 {lang['name']}로 번역한 원문",
              "pinyin": "해당하는 경우 발음 기호(병음 등), 없거나 불필요하면 빈 문자열",
              "translation": "제공된 한국어 문장 (그대로 유지하거나 조금 더 자연스럽게 다듬은 해석)"
            }}
          ],
          "vocabulary": [
            {{
              "word": "핵심 단어",
              "pinyin": "해당하는 경우 발음 기호(병음 등), 없거나 불필요하면 빈 문자열",
              "pos": "품사 (예: [명사])",
              "meaning": "한글 의미"
            }}
          ],
          "collocations": [
            {{
              "expression": "덩어리 표현",
              "pinyin": "해당하는 경우 발음 기호(병음 등), 없거나 불필요하면 빈 문자열",
              "meaning": "한글 의미"
            }}
          ]
        }}
        """

        max_retries = 3
        data = None
        for attempt in range(max_retries):
            try:
                print(f"⏳ AI가 글을 작성하고 분석 중입니다... (시도 {attempt+1}/{max_retries})")
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json",
                    ),
                )
                
                # 마크다운 잔여물 제거
                resp_text = response.text.strip()
                if resp_text.startswith("```json"):
                    resp_text = resp_text[7:]
                if resp_text.endswith("```"):
                    resp_text = resp_text[:-3]
                resp_text = resp_text.strip()
                
                data = json.loads(resp_text)
                break
            except Exception as e:
                print(f"⚠️ {lang['name']} 텍스트 생성 실패 ({attempt+1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    print(f"❌ 최대 재시도 횟수 초과. 해당 언어는 건너뜁니다.")
                else:
                    await asyncio.sleep(10)
        
        if not data:
            continue

        # 워드 파일 저장
        doc_filename = os.path.join(target_folder, f"{lang['name']}_학습자료.docx")
        try:
            create_docx(data, doc_filename, lang['name'], selected_style, selected_topic)
            print(f"✅ 문서 파일 저장 완료: {doc_filename}")
        except Exception as e:
            print(f"❌ 문서 파일 저장 중 오류 발생: {e}")

        # 음성 파일 저장 (대화 형식이므로 남녀 성우 교대로 생성하여 바이너리 병합)
        print(f"🎵 {lang['name']} 음성(TTS) 파일 생성 중 (남녀 듀엣 버전)...")
        audio_filename = os.path.join(target_folder, f"{lang['name']}_학습음성.mp3")
        try:
            temp_files = []
            sentences = [s.get('original', '') for s in data.get('sentences', [])]
            
            for i, sent_text in enumerate(sentences):
                selected_voice = lang['voices'][i % 2]
                temp_fn = f"{audio_filename}_temp_{i}.mp3"
                
                communicate = edge_tts.Communicate(sent_text, selected_voice, rate=lang['rate'])
                await communicate.save(temp_fn)
                temp_files.append(temp_fn)
            
            with open(audio_filename, 'wb') as outfile:
                for temp_fn in temp_files:
                    with open(temp_fn, 'rb') as infile:
                        outfile.write(infile.read())
                    try:
                        os.remove(temp_fn)
                    except:
                        pass
                        
            print(f"✅ 듀엣 음성 파일 저장 완료: {audio_filename}")
        except Exception as e:
            print(f"❌ 음성 파일 저장 중 오류 발생: {e}")
            
        # 다음 언어 API 요청 전 제한 완화를 위해 5초 대기
        await asyncio.sleep(5)

    # GitHub Actions 환경이면 Google Drive에 업로드
    if IS_GITHUB_ACTIONS:
        print("\n☁️ Google Drive에 파일 업로드 중...")
        try:
            service = get_drive_service()
            if service:
                upload_folder_to_drive(service, target_folder, today_folder_name)
                print("✅ Google Drive 업로드 완료!")
            else:
                print("⚠️ Drive 서비스를 초기화할 수 없어 업로드를 건너뜁니다.")
        except Exception as e:
            print(f"❌ Google Drive 업로드 실패: {e}")

    print("\n🎉 모든 언어(영어/중국어)의 작업이 완벽하게 완료되었습니다!")

if __name__ == "__main__":
    asyncio.run(main_async())
