from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..controllers import recommendation_controller
from ..schemas import JobRecommendation

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"]
)

@router.get("/{user_id}", response_model=List[JobRecommendation])
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    return recommendation_controller.get_recommendations(db=db, user_id=user_id) 