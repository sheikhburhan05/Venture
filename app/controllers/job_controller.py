from sqlalchemy.orm import Session
from ..models import Job
from ..schemas import JobCreate
from ..services import job_service

def create_job(db: Session, job: JobCreate):
    return job_service.create_job(db=db, job=job) 