from fastapi import FastAPI
from app.api.routes import router
from app.core.database import Base, engine
from app.models import job

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Job Automation System API running"}