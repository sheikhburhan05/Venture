from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate
from ..services import user_service

def create_user(db: Session, user: UserCreate):
    return user_service.create_user(db=db, user=user) 