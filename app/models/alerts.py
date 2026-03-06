from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(Integer, ForeignKey("videos.id"))
    alert_type = Column(String)
    description = Column(String)