from sqlalchemy.orm import Session
from ..models import JobInteraction
from ..schemas import JobInteractionCreate
from ..services import interaction_service

def create_interaction(db: Session, interaction: JobInteractionCreate):
    return interaction_service.create_interaction(
        db=db,
        interaction=interaction
    ) 