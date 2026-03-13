def filter_jobs(jobs, keyword):

    keyword = keyword.lower()

    filtered_jobs = []

    for job in jobs:
        if keyword in job["title"].lower():
            filtered_jobs.append(job)

    return filtered_jobs