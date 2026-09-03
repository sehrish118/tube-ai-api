from fastapi import APIRouter, Depends
from app.schemas.videos import VideoProcessRequest, VideoProcessResponse
from app.services.video_service import VideoService
from app.dependencies import get_video_service

router = APIRouter(prefix="/videos", tags=["Videos"])


#video_service = VideoService()


@router.post("/process", response_model=VideoProcessResponse)
async def process_video(request: VideoProcessRequest,
                        video_service:VideoService=Depends(get_video_service)):
    result = video_service.process_video(request)
    return result
