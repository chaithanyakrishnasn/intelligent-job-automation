import requests
from app.core.database import SessionLocal
from app.models.job import Job


def scrape_jobs():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    db = SessionLocal()

    saved_jobs = []

    for job in data[1:6]:

        title = job.get("position")
        company = job.get("company")

        existing_job = db.query(Job).filter(
            Job.title == title,
            Job.company == company
        ).first()

        if existing_job:
            continue

        job_obj = Job(
            title=title,
            company=company,
            url=job.get("url"),
            status="new"
        )

        db.add(job_obj)

        saved_jobs.append({
            "title": job_obj.title,
            "company": job_obj.company
        })

    db.commit()
    db.close()

    return saved_jobs