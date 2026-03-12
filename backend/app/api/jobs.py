from fastapi import APIRouter
from app.services.job_scraper import scrape_jobs
from app.core.database import SessionLocal
from app.models.job import Job

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