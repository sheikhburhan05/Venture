from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..controllers import job_controller
from ..schemas import JobCreate, Job

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_controller.create_job(db=db, job=job) 