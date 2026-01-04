from fastapi import APIRouter
router = APIRouter()

jobs = []

@router.post("/")
def create_job(job: dict):
    jobs.append(job)
    return {"message": "Job created"}

@router.get("/")
def list_jobs():
    return jobs
