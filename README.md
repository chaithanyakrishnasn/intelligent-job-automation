Intelligent Job Automation System
An end-to-end AI-assisted job automation platform that combines:
Python-based job scraping FastAPI backend REST APIs SQLAlchemy for database management Resume-based skill extraction Intelligent job matching and recommendation Automated email generation and sending APScheduler for periodic automation

For the current demo:
Job scraping fetches real-time job listings from RemoteOK API
Database stores jobs with duplicate prevention
Resume parsing extracts skills dynamically from user input
Job matching compares extracted skills with job data
Recommendation engine ranks jobs based on match score
Email generator creates personalized job application emails
Email sender sends applications via SMTP
Scheduler automates periodic job scraping

Demo Architecture
backend/
├── app/
│   ├── api/            # API routes (jobs, user, recommendations)
│   ├── services/       # Business logic (scraper, matcher, scorer, email)
│   ├── models/         # Database models (Job, User)
│   ├── core/           # DB config
│   └── main.py         # Entry point
│
├── scheduler/          # APScheduler automation
├── requirements.txt
└── .env
1. Clone the repo
git clone https://github.com/YOUR_USERNAME/intelligent-job-automation.git
cd intelligent-job-automation/backend
2. Setup Environment
Create virtual environment:

python -m venv venv
venv\Scripts\activate   (Windows)
Install dependencies:

pip install -r requirements.txt
3. Run the Backend
uvicorn app.main:app --reload
Access API:

http://127.0.0.1:8000/docs
4. Core Features
Job Scraping
Fetches jobs from RemoteOK API

Extracts title, company, location

Database Storage
Stores jobs using SQLAlchemy

Prevents duplicate entries

Resume Skill Extraction
Parses resume text

Extracts skills using keyword matching

Job Matching & Scoring
Matches jobs with extracted skills

Generates match score (0–100%)

Recommendation Engine
Returns top N jobs sorted by relevance

Supports filtering by minimum score

Application Tracking
Tracks job status (new, applied, interview, etc.)

Email Automation
Generates job application emails

Sends emails using SMTP

Scheduler Automation
Automatically scrapes jobs periodically using APScheduler

5. API Endpoints
Job APIs
GET /jobs                    → Run scraper
GET /jobs/db                → Get stored jobs
PUT /jobs/{id}/status       → Update job status
GET /jobs/filter            → Filter jobs by keyword
Recommendation APIs
POST /jobs/recommendations
GET /jobs/recommendations/{user_id}
Resume & User APIs
POST /resume/skills         → Extract skills
POST /user/profile          → Create user profile
Email APIs
GET /jobs/email/{id}        → Generate email
GET /jobs/send-email/{id}   → Send email
6. Example Flow
Create user profile with resume:

POST /user/profile
Run job scraper:

GET /jobs
Get recommendations:

GET /jobs/recommendations/{user_id}
Generate email:

GET /jobs/email/{job_id}
Send application:

GET /jobs/send-email/{job_id}
7. Example Output
{
  "user": "Krishna",
  "skills": ["python", "fastapi", "sql"],
  "recommendations": [
    {
      "job_title": "Backend Engineer",
      "company": "XYZ",
      "match_score": 75
    }
  ]
}
8. Full Demo Flow
Run scraper manually or via scheduler

System will:

Fetch job listings

Store jobs in database

Extract resume skills

Score jobs based on skills

Rank and recommend jobs

Generate application emails

Send emails automatically

9. What is Real vs Heuristic
Real in current system:
Job scraping (API-based)

Database storage and deduplication

Resume skill extraction

Email generation and sending

Scheduler automation

REST API architecture

Heuristic:
Skill matching (keyword-based)

Scoring logic (simple ratio)

Limited job data (title-based matching)

10. Technologies Used
Python

FastAPI

SQLAlchemy

SQLite / PostgreSQL

APScheduler

SMTP (Email)

REST APIs

11. Future Enhancements
NLP-based resume parsing

Job description-based matching

Machine learning recommendation engine

Frontend dashboard (React)

Multi-user authentication

Deployment with Docker & AWS

Summary
This project demonstrates a full-stack backend automation system that integrates:

Data ingestion → Processing → Intelligence → Automation
and simulates a real-world job recommendation and application assistant.