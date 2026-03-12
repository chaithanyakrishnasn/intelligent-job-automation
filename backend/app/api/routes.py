from fastapi import APIRouter
from app.api.jobs import router as jobs_router

router.include_router(jobs_router)
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}