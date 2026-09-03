from app.services.video_service import VideoService


def get_video_service() -> VideoService:
    return VideoService()
