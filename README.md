# Intelligent Job Automation System

An end-to-end job automation platform that integrates job scraping, resume analysis, job matching, and automated email applications.

---

## Features

- Python-based job scraping  
- FastAPI backend with REST APIs  
- SQLAlchemy ORM for database management  
- Resume-based skill extraction  
- Job matching and recommendation engine  
- Email generation and SMTP-based sending  
- APScheduler for automated periodic execution  

---

## Current Demo Capabilities

- Fetch job listings from RemoteOK API  
- Store jobs with duplicate prevention  
- Extract skills from user resumes  
- Match jobs based on skill relevance  
- Rank jobs using scoring logic  
- Track job application status  
- Generate email drafts for applications  
- Send emails via SMTP  
- Automate scraping using scheduler  

---

## Project Architecture

```
app/
├── api/          # FastAPI endpoints (jobs, recommendations, user profile)
├── services/     # Business logic (scraper, matcher, scorer, email, parser)
├── models/       # Database models (Job, User)
├── core/         # Database configuration

scheduler/
└── scheduler.py  # APScheduler automation
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/intelligent-job-automation.git
cd intelligent-job-automation/backend
```

---

### 2. Setup Environment

Ensure you have:

- Python 3 installed  
- Virtual environment activated  

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Run the Backend

```bash
uvicorn app.main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

## Core Features Breakdown

- Job scraping retrieves job listings from API  
- Database stores jobs with deduplication logic  
- Resume parsing extracts skills dynamically  
- Job matching compares skills with job titles  
- Scoring system generates match percentage  
- Recommendation engine ranks jobs by relevance  
- Application tracking updates job lifecycle status  
- Email generator creates application templates  
- SMTP integration sends application emails  
- Scheduler automates periodic scraping  

---

## API Endpoints

### Job APIs

- `GET /jobs`
- `GET /jobs/db`
- `PUT /jobs/{id}/status`
- `GET /jobs/filter`

### Recommendation APIs

- `POST /jobs/recommendations`
- `GET /jobs/recommendations/{user_id}`

### Resume & User APIs

- `POST /resume/skills`
- `POST /user/profile`

### Email APIs

- `GET /jobs/email/{id}`
- `GET /jobs/send-email/{id}`

---

## Example Workflow

### 1. Create User Profile

```json
POST /user/profile
{
  "name": "Krishna",
  "text": "Python FastAPI backend SQL Docker"
}
```

---

### 2. Run Job Scraper

```
GET /jobs
```

---

### 3. Get Recommendations

```
GET /jobs/recommendations/{user_id}
```

---

### 4. Generate Email

```
GET /jobs/email/{job_id}
```

---

### 5. Send Application

```
GET /jobs/send-email/{job_id}
```

---

## Example Output

```json
[
  {
    "job_title": "Backend Engineer",
    "company": "XYZ",
    "match_score": 75
  }
]
```

---

## Full Demo Flow

The system can run manually or via scheduler:

1. Fetch job listings  
2. Store jobs in database  
3. Extract resume skills  
4. Evaluate job relevance  
5. Rank jobs based on score  
6. Generate application emails  
7. Send emails automatically  

---

## Real vs Heuristic Components

### Real Implementations

- Job scraping via API  
- Database storage and deduplication  
- Resume skill extraction  
- Email generation and sending  
- Scheduler automation  
- REST API architecture  

### Heuristic Components

- Keyword-based matching  
- Basic scoring logic  
- Title-based job evaluation  

---

## Best Demo Mode

For the best demonstration:

- Input resume with backend-related skills  
- Run scraper to populate jobs  
- Generate recommendations  
- Update job status  
- Generate and send email  
- Demonstrate automated scheduling  

---

## Technologies Used

- Python  
- FastAPI  
- SQLAlchemy  
- SQLite / PostgreSQL  
- APScheduler  
- SMTP  
- REST APIs  

---

## Future Enhancements

- NLP-based resume parsing  
- Job description-based matching  
- Machine learning recommendation engine  
- Frontend dashboard  
- User authentication system  
- Docker deployment  
- Cloud hosting  

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss proposed updates.

---

## Support

If you found this project useful, consider giving it a star on GitHub.
