from pydantic import BaseModel


class TranscriptSegment(BaseModel):
    text:str
    start:float
    duration:float


class VideoTranscript(BaseModel):
    video_id:str
    language:str
    segments:list[TranscriptSegment]

