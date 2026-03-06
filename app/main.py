from fastapi import FastAPI, HTTPException
from app.database import Base, engine
from app.routers import videos, dashboard

# IMPORTANT: Import models
from app.models import train, camera, video, ai_detection, alerts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Railway CCTV Monitoring API")

app.include_router(videos.router)
app.include_router(dashboard.router)

@app.get("/")
def home():
    return {"message": "Railway CCTV API Running"}