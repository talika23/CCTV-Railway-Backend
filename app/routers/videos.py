from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import video_service
from app.schemas.video_schema import VideoCreate

router = APIRouter(prefix="/api/videos", tags=["Videos"])


@router.get("/")
def get_videos(db: Session = Depends(get_db)):
    videos = video_service.get_videos(db)
    return {"data": videos}


@router.get("/{video_id}")
def get_video(video_id: int, db: Session = Depends(get_db)):
    video = video_service.get_video(db, video_id)
    return {"data": video}


@router.post("/")
def create_video(video: VideoCreate, db: Session = Depends(get_db)):
    new_video = video_service.create_video(db, video)
    return {
        "message": "Video created successfully",
        "data": new_video
    }


# =========================
# UPDATE VIDEO API
# =========================

@router.put("/{video_id}")
def update_video(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):

    updated_video = video_service.update_video(db, video_id, video)

    if not updated_video:
        raise HTTPException(status_code=404, detail="Video not found")

    return {
        "message": "Video updated successfully",
        "data": updated_video
    }


# =========================
# DELETE VIDEO API
# =========================

@router.delete("/{video_id}")
def delete_video(video_id: int, db: Session = Depends(get_db)):

    deleted = video_service.delete_video(db, video_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Video not found")

    return {
        "message": "Video deleted successfully"
    }
# from fastapi import APIRouter, Depends
# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.services import video_service
# from app.schemas.video_schema import VideoCreate

# router = APIRouter(prefix="/api/videos", tags=["Videos"])


# @router.get("/")
# def get_videos(db: Session = Depends(get_db)):
#     videos = video_service.get_videos(db)
#     return {"data": videos}


# @router.get("/{video_id}")
# def get_video(video_id: int, db: Session = Depends(get_db)):
#     video = video_service.get_video(db, video_id)
#     return {"data": video}


# @router.post("/")
# def create_video(video: VideoCreate, db: Session = Depends(get_db)):
#     new_video = video_service.create_video(db, video)
#     return {
#         "message": "Video created successfully",
#         "data": new_video
#     }