from fastapi import APIRouter
from app.services.job_scraper import scrape_jobs
from app.core.database import SessionLocal
from app.models.job import Job
from pydantic import BaseModel
from fastapi import Query
from app.services.job_filter import filter_jobs

router = APIRouter()

@router.get("/jobs")
def run_scraper():
    return scrape_jobs()


@router.get("/jobs/db")
def get_jobs_from_db():
    db = SessionLocal()

    jobs = db.query(Job).all()

    result = []

    for job in jobs:
        result.append({
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "status": job.status
        })

    db.close()

    return result

class StatusUpdate(BaseModel):
    status: str


@router.put("/jobs/{job_id}/status")
def update_job_status(job_id: int, payload: StatusUpdate):

    db = SessionLocal()

    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    job.status = payload.status

    db.commit()
    db.close()

    return {"message": "Status updated", "job_id": job_id, "status": payload.status}

@router.get("/jobs/filter")
def filter_jobs_endpoint(keyword: str = Query(...)):

    jobs = scrape_jobs()

    return filter_jobs(jobs, keyword)