from app.integrations.youtube_audio import YouTubeAudioDownloader
from app.integrations.whisper_client import WhisperClient


video_id = "oRcLYB8vaf4"

# Step 1: Download audio
downloader = YouTubeAudioDownloader()

audio_path = downloader.download(video_id)

print("Audio downloaded:")
print(audio_path)


# Step 2: Transcribe audio
whisper = WhisperClient()

segments, info = whisper.transcribe(audio_path)

print("\nDetected language:")
print(info.language)

print("\n===== TRANSCRIPT =====")

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text.strip()}")
