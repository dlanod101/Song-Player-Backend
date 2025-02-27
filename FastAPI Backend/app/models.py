from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class SongModel(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    artiste = Column(String(100), nullable=False)
    is_liked = Column(Boolean, default=False)
    audio_url = Column(String(100), nullable=False)
    image = Column(String(100), nullable=False)