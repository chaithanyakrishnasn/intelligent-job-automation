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
        job_obj = Job(
            title=job.get("position"),
            company=job.get("company"),
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