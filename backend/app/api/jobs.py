from fastapi import APIRouter
from app.services.job_scraper import scrape_jobs

router = APIRouter()

@router.get("/jobs")
def get_jobs():
    return scrape_jobs()