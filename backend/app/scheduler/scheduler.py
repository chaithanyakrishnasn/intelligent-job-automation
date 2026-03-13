from apscheduler.schedulers.background import BackgroundScheduler
from app.services.job_scraper import scrape_jobs

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(scrape_jobs, "interval", hours=3)
    scheduler.start()