# Train CCTV Monitoring Dashboard - Backend

## Project Overview
This project is the backend for a Train CCTV Monitoring Dashboard.  
It is built using **FastAPI** and **PostgreSQL** to manage CCTV video metadata, AI detection results, and alerts.  
The system provides REST APIs to fetch video information and dashboard summary metrics.

---

## Tech Stack
- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Server:** Uvicorn  
- **Video Storage:** AWS S3 (video links stored in DB)  
- **API Documentation:** Swagger UI (`/docs`)

---

## Project Structure
app/
├── routers/ # API endpoints
│ └── videos.py
├── services/ # Business logic / database operations
│ └── video_service.py
├── models/ # Database models (SQLAlchemy)
├── schemas/ # Request & Response validation (Pydantic)
├── database.py # Database connection and initialization
└── main.py # FastAPI app initialization


---

## Database Schema

**Tables:**

| Table Name      | Description |
|-----------------|-------------|
| `trains`        | Stores train information |
| `cameras`       | Stores camera info per train |
| `videos`        | Stores metadata and S3 video URLs |
| `ai_detections` | AI detection results per video |
| `alerts`        | Generated alerts based on AI detections |

**Relationships:**
- Each train can have multiple cameras.  
- Each camera generates multiple videos.  
- AI detection results are linked to videos.  
- Alerts are generated based on AI detections.

---

## API Endpoints

**Base URL:** `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/api/videos` | Fetch all stored videos |
| GET    | `/api/videos/{video_id}` | Fetch details of a specific video |
| POST   | `/api/videos` | Create a new video record |
| GET    | `/api/dashboard/summary` | Fetch dashboard metrics (total videos, monitored trains, alerts, storage usage) |

**Example Response (GET /api/videos/{id}):**
```json
{
  "train_number": "12345",
  "camera_id": "101",
  "video_url": "https://s3.amazonaws.com/...",
  "status": "available",
  "ai_detections": []
}

Running the Project

Clone the repository

git clone <your-repo-link>
cd train-cctv-backend

Create virtual environment

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

Install dependencies

pip install -r requirements.txt

Setup PostgreSQL

Create database and tables (SQLAlchemy can auto-create if not exist).

Update database.py with your DB credentials.

Run server

uvicorn app.main:app --reload

Swagger API Docs

Open: http://127.0.0.1:8000/docs

Test APIs interactively.


ER Diagram & Architecture

ER Diagram: image & recordings/ER Diagram.jpg

Architecture Improvements: image & recordings/Architecture Improvements.pdf

Key Architecture Improvements:

AWS S3 for video storage to reduce DB load

Modular API structure for maintainability

Indexing for faster queries

Structured logging for monitoring

## Videos

**UI Demo:** [Google Drive Link](https://drive.google.com/file/d/1gSe8COHuuUoHEAIIKt9_LcHE98QhX8Lq/view?usp=sharing)  
**Technical Walkthrough:** [Google Drive Link](https://drive.google.com/file/d/1VL4QBS3UySF78Q85FztwZwB3nid_tFdu/view?usp=sharing)