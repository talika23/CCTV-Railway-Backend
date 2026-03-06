from pydantic import BaseModel
from datetime import datetime


class VideoCreate(BaseModel):
    train_id: int
    camera_id: int
    video_url: str
    status: str
    ai_status: str


class VideoResponse(BaseModel):
    id: int
    train_id: int
    camera_id: int
    video_url: str
    stored_timestamp: datetime
    status: str
    ai_status: str

    class Config:
        orm_mode = True