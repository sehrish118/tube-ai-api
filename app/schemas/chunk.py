from pydantic import BaseModel


class TextChunk(BaseModel):
    chunk_id:str
    video_id:str
    text:str
    start_time:float
    end_time:float
    chunk_index:int


#Why start and end_time
#This enables: (citation,youtube timestamp links,source attribution,better answers)
