import requests


def scrape_jobs():
    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    jobs = []

    for job in data[1:6]:   # skip first metadata object
        jobs.append({
            "title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location"),
        })

    return jobs