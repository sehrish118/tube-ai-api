from app.integrations.youtube_audio import YouTubeAudioDownloader


video_id = "0KGP9f3duEg"

downloader = YouTubeAudioDownloader()

audio_path = downloader.download(video_id)

print("Downloaded audio:")
print(audio_path)
