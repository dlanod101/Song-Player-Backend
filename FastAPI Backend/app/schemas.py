from pydantic import BaseModel
from typing import List


class SongBase(BaseModel):
    title: str
    image: str
    artiste: str
    is_liked: bool
    audio_url: str

    # class Config:
    #     orm_mode: True

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        from_attributes = True

class SongList(BaseModel):
    song_ids: List[int]