from app.services.job_scorer import score_job


def recommend_jobs(jobs, skills):

    scored_jobs = []

    for job in jobs:
        result = score_job(job, skills)

        scored_jobs.append({
            "job_title": job.title,
            "company": job.company,
            "match_score": result["match_score"]
        })

    scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    return scored_jobs