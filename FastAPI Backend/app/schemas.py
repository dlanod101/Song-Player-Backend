from pydantic import BaseModel
from typing import List


class Song(BaseModel):
    id: int
    title: str
    image: str
    artiste: str
    is_liked: bool
    audio_url: str

class Songs(BaseModel):
    songs: List[Song]