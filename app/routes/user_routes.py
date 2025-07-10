from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..controllers import user_controller
from ..schemas import UserCreate, User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db=db, user=user) 