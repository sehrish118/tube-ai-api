from pydantic import BaseModel, HttpUrl


class VideoProcessRequest(BaseModel):
    youtube_url: HttpUrl


class VideoProcessResponse(BaseModel):
    video_id: str
    status: str
    chunks_created: int
