skills = ["python", "fastapi", "backend", "api", "sql", "docker", "Docker", "kubernetes", "aws", "azure", "gcp", "cloud", "devops", "ci/cd", "git", "github", "gitlab"]



def score_job(job, skills):

    text = f"{job.title} {job.company}".lower()

    matched = []

    for skill in skills:
        if skill in text:
            matched.append(skill)

    score = int((len(matched) / len(skills)) * 100) if skills else 0

    return {
        "job_title": job.title,
        "match_score": score,
        "matched_skills": matched
    }