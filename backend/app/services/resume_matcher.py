skills = ["python", "fastapi", "backend", "api", "sql", "docker"]


def match_job(job):

    title = job.title.lower()

    for skill in skills:
        if skill in title:
            return {
                "match": True,
                "matched_skill": skill
            }

    return {
        "match": False
    }