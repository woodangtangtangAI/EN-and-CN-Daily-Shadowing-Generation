import sys
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        text = " ".join([t['text'] for t in transcript])
        with open("transcript.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Transcript saved to transcript.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_transcript("oJhU1IGTdoo")
