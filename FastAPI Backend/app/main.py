import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Songs, Song


app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_certificates=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

memory_db = {"songs": []}

@app.get("/")
def index():
    return {"Message": "Hello World!"}

@app.get("/list", response_model=Songs)
def get_songs():
    return Songs(songs=memory_db["songs"])

@app.get("/get/{song_id}", response_model=Song)
def get_song(song_id: int):
    for song in memory_db["songs"]:
        if song.id == song_id:
            return song
    return {"error": "Song not found"}

@app.post("/songs", response_model=Song)
def add_song(song: Song):
    memory_db["songs"].append(song)
    return song

@app.put("/update/{song_id}", response_model=Song)
def update_song(song_id: int, song_obj:Song):
    for index, song in enumerate(memory_db["songs"]):
        if song.id == song_id:
            memory_db["songs"][index] = song_obj
            return song_obj
    return {"error": "Song not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)