from pydantic import BaseModel, Field
# pydantic:Incoming data ko validate or structure krna


# Field(...) -> means this field is required


# Request: Client -> backend
class AskRequest(BaseModel):
    video_id: str = Field(..., min_length=1, description="YouTube video ID")

    question: str = Field(..., min_length=1, description="Question about the video")


# Response: Backend -> Client
class AskResponse(BaseModel):
    video_id: str
    question: str
    answer: str
