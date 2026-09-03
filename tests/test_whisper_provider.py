from app.integrations.youtube_audio import YouTubeAudioDownloader
from app.services.whisper_transcript_provider import WhisperTranscriptProvider


video_id = "oRcLYB8vaf4"

downloader = YouTubeAudioDownloader()

audio_path = downloader.download(video_id)

print("Audio downloaded:")
print(audio_path)


provider = WhisperTranscriptProvider()

transcript = provider.get_transcript(
    video_id=video_id,
    audio_path=audio_path,
)


print("\n===== RESULT =====")

print("Video ID:", transcript.video_id)
print("Language:", transcript.language)
print("Total segments:", len(transcript.segments))


print("\n===== FIRST 5 SEGMENTS =====")

for segment in transcript.segments[:5]:
    print(
        f"[{segment.start:.2f}s -> "
        f"{segment.start + segment.duration:.2f}s] "
        f"{segment.text}"
    )
