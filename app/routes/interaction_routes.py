from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..controllers import interaction_controller
from ..schemas import JobInteractionCreate, JobInteraction

router = APIRouter(
    prefix="/interactions",
    tags=["interactions"]
)

@router.post("/", response_model=JobInteraction)
def create_interaction(
    interaction: JobInteractionCreate,
    db: Session = Depends(get_db)
):
    return interaction_controller.create_interaction(
        db=db,
        interaction=interaction
    ) 