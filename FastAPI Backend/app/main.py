import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
from database import engine, Base
from api.routes import router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    return database.get_db()

@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"Hello": "World"}

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)