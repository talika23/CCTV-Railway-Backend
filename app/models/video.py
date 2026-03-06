from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    train_id = Column(Integer, ForeignKey("trains.id"))
    camera_id = Column(Integer)
    video_url = Column(String)
    stored_timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String)
    ai_status = Column(String)