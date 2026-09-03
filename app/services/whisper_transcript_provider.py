from app.integrations.whisper_client import WhisperClient
from app.schemas.transcript import VideoTranscript, TranscriptSegment


class WhisperTranscriptProvider:
    def __init__(self):
        self.client = WhisperClient()

    def get_transcript(
        self,
        video_id: str,
        audio_path: str,
    ) -> VideoTranscript:

        segments, info = self.client.transcribe(audio_path)

        transcript_segments = []

        for segment in segments:
            transcript_segments.append(
                TranscriptSegment(
                    text=segment.text.strip(),
                    start=segment.start,
                    duration=segment.end - segment.start,
                )
            )

        return VideoTranscript(
            video_id=video_id,
            language=info.language,
            segments=transcript_segments,
        )
