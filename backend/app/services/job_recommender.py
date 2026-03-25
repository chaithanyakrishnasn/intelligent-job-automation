from app.services.job_scorer import score_job


def recommend_jobs(jobs, skills, limit=5, min_score=0):

    scored_jobs = []

    for job in jobs:
        result = score_job(job, skills)

        if result["match_score"] >= min_score:
            scored_jobs.append({
                "job_title": job.title,
                "company": job.company,
                "match_score": result["match_score"]
            })

    scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    return scored_jobs[:limit]