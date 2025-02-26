from fastapi import APIRouter
from schemas import Songs, Song
from typing import List

router = APIRouter()

memory_db = {"songs": []}


@router.get("/")
def index():
    return {"Message": "Hello World!"}


@router.get("/list", response_model=Songs)
def get_songs():
    return Songs(songs=memory_db["songs"])


@router.get("/get/{song_id}", response_model=Song)
def get_song(song_id: int):
    for song in memory_db["songs"]:
        if song.id == song_id:
            return song
    return {"error": "Song not found"}


@router.post("/songs", response_model=Song)
def add_song(song: Song):
    memory_db["songs"].append(song)
    return song


@router.put("/update/{song_id}", response_model=Song)
def update_song(song_id: int, song_obj: Song):
    for index, song in enumerate(memory_db["songs"]):
        if song.id == song_id:
            memory_db["songs"][index] = song_obj
            return song_obj
    return {"error": "Song not found"}


@router.delete("/delete/{song_id}", response_model=Song)
def delete_song(song_id: int):
    for index, song in enumerate(memory_db["songs"]):
        if song.id == song_id:
            deleted_song = memory_db["songs"].pop(index)
            return deleted_song
    return {"error": "Song not found"}

@router.delete("/select_delete/")
def delete_selected_songs(song_ids: List[int]):
    for song_id in song_ids:
        for index, song in enumerate(memory_db["songs"]):
            if song.id == song_id:
                memory_db["songs"].pop(index)
    return {"message": "Selected songs deleted"} 

@router.delete("/delete/")
def delete_all_songs():
    memory_db["songs"] = []
    return {"message": "All songs deleted"}