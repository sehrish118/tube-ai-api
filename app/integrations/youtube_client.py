from youtube_transcript_api import (
    YouTubeTranscriptApi,
)  # class import from external packages
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

from app.schemas.transcript import TranscriptSegment, VideoTranscript
from app.exceptions.transcript import TranscriptNotAvailable, TranscriptFetchError


class YouTubeClient:
    def get_transcript(
        self, video_id: str
    ) -> VideoTranscript:  # define return type hint
        try:
            api = YouTubeTranscriptApi()

            transcript = api.fetch(video_id)  # retrieve transcript from external system
            #                   transcript
            #                       ↓
            #                External library ka object

            # List comprehension (External Segment -> Transcript Segment)
            segments = [
                TranscriptSegment(
                    text=item.text, start=item.start, duration=item.duration
                )
                for item in transcript
            ]
            return VideoTranscript(
                video_id=video_id, language=transcript.language_code, segments=segments
            )

        except (TranscriptsDisabled, NoTranscriptFound) as exc:
            raise TranscriptNotAvailable(
                "Transcript is not available for this video"
            ) from exc

        except VideoUnavailable as exc:
            raise TranscriptFetchError("The YouTube Video is unavailable") from exc

        except Exception as exc:
            raise TranscriptFetchError(
                "Failed to fetch the video transcript"
            ) from exc  # here, we are sending custom messages to our exception
