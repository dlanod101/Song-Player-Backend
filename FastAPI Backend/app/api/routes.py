from fastapi import APIRouter, Depends, HTTPException, status
from schemas import Song, SongCreate, SongBase, SongList
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from models import SongModel

router = APIRouter()

# Index route
@router.get("/")
def index():
    return {"Message": "Hello World!"}

# Get all songs
@router.get("/list", response_model=List[Song])
def read_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    songs = db.query(SongModel).offset(skip).limit(limit).all()
    return songs

# Get a song
@router.get("/get/{song_id}", response_model=Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    song = db.query(SongModel).filter(SongModel.id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

# Add a song
@router.post("/create/", response_model=Song)
def add_song(song: SongBase, db: Session = Depends(get_db)):
    db_song = SongModel(**song.model_dump())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

# Update a song
@router.put("/update/{song_id}", response_model=Song)
def update_song(song_id: int, song: SongCreate, db: Session = Depends(get_db)):
    db_song = db.query(SongModel).filter(SongModel.id == song_id).first()
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")

    for key, value in song.dict().items():
        setattr(db_song, key, value)

    db.commit()
    db.refresh(db_song)
    return db_song

# Delete a song
@router.delete("/delete/{song_id}", response_model=Song)
def delete_song(song_id: int, db: Session = Depends(get_db)):
    db_song = db.query(SongModel).filter(SongModel.id == song_id).first()
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")

    db.delete(db_song)
    db.commit()
    return db_song

# Delete selected songs
@router.delete("/select_delete/", status_code=status.HTTP_200_OK)
def delete_selected_songs(song_list: SongList, db: Session = Depends(get_db)):
    try:
        # Delete songs with IDs in the list
        deleted_count = (
            db.query(SongModel)
            .filter(SongModel.id.in_(song_list.song_ids))
            .delete(synchronize_session=False)
        )

        db.commit()

        if deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No songs found with the provided IDs",
            )

        return {
            "message": f"Successfully deleted {deleted_count} songs",
            "deleted_count": deleted_count,
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

# Delete all songs
@router.delete("/delete_all/")
def delete_all_songs(db: Session = Depends(get_db)):
    db_songs = db.query(SongModel).all()

    for db_song in db_songs:
        db.delete(db_song)

    db.commit()
    return {"message": "All songs have been deleted"}