from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.video import Video

router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):

    total_videos = db.query(Video).count()

    return {
        "total_videos_today": total_videos,
        "total_trains_monitored": 5,
        "alerts_generated": 2,
        "storage_usage": "10GB"
    }