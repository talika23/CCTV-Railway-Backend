from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)
    camera_id = Column(String)
    train_id = Column(Integer, ForeignKey("trains.id"))
    location = Column(String)