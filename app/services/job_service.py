from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models import Job
from ..schemas import JobCreate

def create_job(db: Session, job: JobCreate):
    try:
        db_job = Job(
            title=job.title,
            description=job.description,
            required_skills=job.required_skills
        )
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating job: {str(e)}"
        ) 