from sqlalchemy import Column, Integer, String
from app.database import Base

class Train(Base):
    __tablename__ = "trains"

    id = Column(Integer, primary_key=True, index=True)
    train_number = Column(String, unique=True)
    name = Column(String)