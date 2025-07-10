from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models import JobInteraction, User, Job
from ..schemas import JobInteractionCreate

def create_interaction(db: Session, user_id: int, interaction: JobInteractionCreate):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        job = db.query(Job).filter(Job.id == interaction.job_id).first()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        db_interaction = JobInteraction(
            user_id=user_id,
            job_id=interaction.job_id,
            interaction_type=interaction.interaction_type
        )
        db.add(db_interaction)
        db.commit()
        db.refresh(db_interaction)
        return db_interaction
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating interaction: {str(e)}"
        ) 