from fastapi import APIRouter, Query
from pydantic import BaseModel

from app.services.job_scraper import scrape_jobs
from app.services.job_filter import filter_jobs
from app.services.email_generator import generate_email
from app.services.resume_matcher import match_job
from app.services.email_sender import send_email
from app.services.job_scorer import score_job
from app.services.job_recommender import recommend_jobs
from app.services.resume_parser import extract_skills

from app.core.database import SessionLocal
from app.models.job import Job
from app.models.user import User

router = APIRouter()

# -----------------------------
# JOB SCRAPER
# -----------------------------
@router.get("/jobs")
def run_scraper():
    return scrape_jobs()


# -----------------------------
# GET JOBS FROM DB
# -----------------------------
@router.get("/jobs/db")
def get_jobs_from_db():
    db = SessionLocal()
    jobs = db.query(Job).all()

    result = [
        {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "status": job.status
        }
        for job in jobs
    ]

    db.close()
    return result


# -----------------------------
# UPDATE STATUS
# -----------------------------
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


# -----------------------------
# FILTER JOBS
# -----------------------------
@router.get("/jobs/filter")
def filter_jobs_endpoint(keyword: str = Query(...)):
    jobs = scrape_jobs()
    return filter_jobs(jobs, keyword)


# -----------------------------
# EMAIL GENERATION
# -----------------------------
@router.get("/jobs/email/{job_id}")
def generate_job_email(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    email = generate_email(job)
    db.close()
    return email


# -----------------------------
# MATCH JOB WITH RESUME
# -----------------------------
@router.get("/jobs/match/{job_id}")
def match_job_with_resume(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    result = match_job(job)
    db.close()
    return result


# -----------------------------
# SEND EMAIL
# -----------------------------
@router.get("/jobs/send-email/{job_id}")
def send_job_email(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    email_data = generate_email(job)

    result = send_email(
        "recruiter@example.com",
        email_data["subject"],
        email_data["body"]
    )

    db.close()
    return result


# -----------------------------
# JOB SCORING (BASIC)
# -----------------------------
@router.get("/jobs/score/{job_id}")
def score_job_endpoint(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"error": "Job not found"}

    # Using empty skills fallback
    result = score_job(job, [])

    db.close()
    return result


# -----------------------------
# RESUME INPUT MODEL
# -----------------------------
class ResumeInput(BaseModel):
    text: str


# -----------------------------
# EXTRACT SKILLS
# -----------------------------
@router.post("/resume/skills")
def get_resume_skills(payload: ResumeInput):
    skills = extract_skills(payload.text)
    return {"skills": skills}


# -----------------------------
# RECOMMENDATION (WITH FILTERS)
# -----------------------------
@router.post("/jobs/recommendations")
def get_recommendations(
    payload: ResumeInput,
    limit: int = Query(5),
    min_score: int = Query(0)
):
    skills = extract_skills(payload.text)

    db = SessionLocal()
    jobs = db.query(Job).all()

    recommendations = recommend_jobs(jobs, skills, limit, min_score)

    db.close()

    return {
        "skills": skills,
        "recommendations": recommendations
    }


# -----------------------------
# USER PROFILE MODEL
# -----------------------------
class UserProfile(BaseModel):
    name: str
    text: str


# -----------------------------
# CREATE USER PROFILE
# -----------------------------
@router.post("/user/profile")
def create_user_profile(payload: UserProfile):
    skills = extract_skills(payload.text)

    db = SessionLocal()

    user = User(
        name=payload.name,
        skills=",".join(skills)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return {
        "user_id": user.id,
        "name": user.name,
        "skills": skills
    }


# -----------------------------
# RECOMMENDATIONS FOR USER
# -----------------------------
@router.get("/jobs/recommendations/{user_id}")
def get_recommendations_for_user(user_id: int):
    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    skills = user.skills.split(",")

    jobs = db.query(Job).all()

    recommendations = recommend_jobs(jobs, skills)

    db.close()

    return {
        "user": user.name,
        "skills": skills,
        "recommendations": recommendations
    }