from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from ..models import User
from ..schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    try:
        db_user = User(
            name=user.name,
            email=user.email,
            skills=user.skills
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating user: {str(e)}"
        ) 