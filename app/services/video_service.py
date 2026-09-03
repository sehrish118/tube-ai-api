from app.schemas.videos import VideoProcessRequest
from app.utils.youtube import extract_video_id
from app.exceptions.video import InvalidYoutubeURL
from app.services.ingestion_service import IngestionService
from app.services.transcript_service import TranscriptService


class VideoService:
    def __init__(self):
        self.transcript_service = TranscriptService()
        self.ingestion_service = IngestionService()

    def process_video(self, request: VideoProcessRequest) -> dict:

        youtube_url = str(request.youtube_url)

        video_id = extract_video_id(youtube_url)

        if not video_id:
            raise InvalidYoutubeURL()

        transcript = self.transcript_service.get_transcript(video_id)

        self.ingestion_service.ingest(transcript)

        chunks_created = self.ingestion_service.ingest(transcript)

        return {
            "video_id": video_id,
            "status": "processed",
            "chunks_created": chunks_created,
        }
