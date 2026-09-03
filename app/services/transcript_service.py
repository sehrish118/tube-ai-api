# from app.integrations.youtube_client import YouTubeClient
# from app.schemas.transcript import VideoTranscript


# class TranscriptService:
#     def __init__(self):
#         self.youtube_client = YouTubeClient()

#     def get_transcript(self, video_id: str) -> VideoTranscript:
#         return self.youtube_client.get_transcript(video_id)

#     def clean_transcript(self, transcript: VideoTranscript) -> str:
#         text = " ".join(
#             segment.text for segment in transcript.segments
#         )  # iterate through each transcript segment text, process each segment one by one
#         return " ".join(text.split())


import os

from app.integrations.youtube_client import YouTubeClient
from app.integrations.youtube_audio import YouTubeAudioDownloader
from app.services.whisper_transcript_provider import WhisperTranscriptProvider
from app.schemas.transcript import VideoTranscript


class TranscriptService:
    def __init__(self):
        self.youtube_client = YouTubeClient()
        self.audio_downloader = YouTubeAudioDownloader()
        self.whisper_provider = WhisperTranscriptProvider()

    def get_transcript(self, video_id: str) -> VideoTranscript:

        try:
            return self.youtube_client.get_transcript(video_id)

        except Exception:
            print("YouTube transcript unavailable. Falling back to Whisper...")

            audio_path = self.audio_downloader.download(video_id)

            try:
                return self.whisper_provider.get_transcript(
                    video_id=video_id,
                    audio_path=audio_path,
                )

            finally:
                self._cleanup_audio(audio_path)

    def _cleanup_audio(self, audio_path: str) -> None:

        try:
            if os.path.exists(audio_path):
                os.remove(audio_path)

            temp_dir = os.path.dirname(audio_path)

            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)

        except OSError:
            pass

    def clean_transcript(
        self,
        transcript: VideoTranscript,
    ) -> str:

        text = " ".join(segment.text for segment in transcript.segments)

        return " ".join(text.split())
