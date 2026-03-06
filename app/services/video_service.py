from sqlalchemy.orm import Session
from app.models.video import Video
from datetime import datetime


def get_videos(db: Session):
    return db.query(Video).all()


def get_video(db: Session, video_id: int):
    return db.query(Video).filter(Video.id == video_id).first()


def create_video(db: Session, video):
    new_video = Video(
        train_id=video.train_id,
        camera_id=video.camera_id,
        video_url=video.video_url,
        stored_timestamp=datetime.utcnow(),
        status=video.status,
        ai_status=video.ai_status
    )

    db.add(new_video)
    db.commit()
    db.refresh(new_video)

    return new_video

# =========================
# UPDATE VIDEO
# =========================

def update_video(db: Session, video_id: int, video):

    db_video = db.query(Video).filter(Video.id == video_id).first()

    if not db_video:
        return None

    db_video.train_id = video.train_id
    db_video.camera_id = video.camera_id
    db_video.video_url = video.video_url
    db_video.status = video.status
    db_video.ai_status = video.ai_status

    db.commit()
    db.refresh(db_video)

    return db_video


# =========================
# DELETE VIDEO
# =========================

def delete_video(db: Session, video_id: int):

    db_video = db.query(Video).filter(Video.id == video_id).first()

    if not db_video:
        return False

    db.delete(db_video)
    db.commit()

    return True