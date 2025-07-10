from sqlalchemy.orm import Session
from typing import List
from ..schemas import JobRecommendation
from ..services import recommendation_service

def get_recommendations(db: Session, user_id: int) -> List[JobRecommendation]:
    return recommendation_service.get_recommendations(db=db, user_id=user_id) 