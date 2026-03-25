skills = ["python", "fastapi", "backend", "api", "sql", "docker", "Docker", "kubernetes", "aws", "azure", "gcp", "cloud", "devops", "ci/cd", "git", "github", "gitlab"]


def score_job(job):

    title = job.title.lower()

    matched = []

    for skill in skills:
        if skill in title:
            matched.append(skill)

    score = int((len(matched) / len(skills)) * 100)

    return {
        "job_title": job.title,
        "match_score": score,
        "matched_skills": matched
    }