# 🧠 Daily Language Learning (자동 영어/중국어 학습 자료 생성기)

매일 새벽 GitHub Actions가 자동으로 영어/중국어 학습 자료(Word 문서 + 듀엣 음성 MP3)를 생성하고, Google Drive에 업로드합니다.

## 🚀 초기 설정 가이드

### 1단계: Google Cloud 서비스 계정 만들기

1. [Google Cloud Console](https://console.cloud.google.com/) 접속 후 로그인
2. 왼쪽 상단 **프로젝트 선택** → **새 프로젝트** 클릭
   - 프로젝트 이름: `daily-language-learning` (원하는 이름 아무거나 OK)
   - **만들기** 클릭
3. 해당 프로젝트가 선택된 상태에서, 왼쪽 메뉴 **APIs 및 서비스** → **라이브러리**
   - 검색창에 `Google Drive API` 입력 → 클릭 → **사용** 버튼 클릭
4. 왼쪽 메뉴 **IAM 및 관리자** → **서비스 계정**
   - **+ 서비스 계정 만들기** 클릭
   - 서비스 계정 이름: `drive-uploader` (아무거나 OK)
   - **만들기 및 계속** → **완료** 클릭
5. 생성된 서비스 계정 목록에서 방금 만든 계정의 이메일 클릭
   - 예: `drive-uploader@daily-language-learning.iam.gserviceaccount.com`
6. 상단 **키** 탭 → **키 추가** → **새 키 만들기** → **JSON** 선택 → **만들기**
   - JSON 파일이 자동 다운로드됩니다 (이 파일을 안전하게 보관!)

### 2단계: Google Drive 폴더 공유

1. Google Drive에서 `[언어 공부]` 폴더를 우클릭 → **공유**
2. 위 5번에서 확인한 서비스 계정 이메일을 입력
   - 예: `drive-uploader@daily-language-learning.iam.gserviceaccount.com`
3. **편집자** 권한으로 공유 → **보내기**

### 3단계: GitHub Secrets 등록

이 저장소의 **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

| Secret 이름 | 값 |
|---|---|
| `GEMINI_API_KEY` | Gemini API 키 (예: `AIzaSy...`) |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | 1단계에서 다운로드한 JSON 파일의 **전체 내용**을 복사-붙여넣기 |

### 4단계: 테스트

1. 이 저장소의 **Actions** 탭 클릭
2. 왼쪽에서 **Daily Language Learning** 워크플로우 클릭
3. **Run workflow** 버튼 클릭 → **Run workflow** 확인
4. 실행 완료 후, Google Drive `[언어 공부]` 폴더에 오늘 날짜 폴더 확인!

## 📂 생성되는 파일 구조

```
[언어 공부]/
├── 20260524 (토)/
│   ├── 영어_학습자료.docx
│   ├── 영어_학습음성.mp3
│   ├── 중국어_학습자료.docx
│   └── 중국어_학습음성.mp3
├── 20260525 (일)/
│   └── ...
```

## ⏰ 자동 실행 시간

- 매일 **새벽 2시 (한국 시간, KST)** 자동 실행
- GitHub Actions 탭에서 **Run workflow** 버튼으로 수동 실행도 가능
