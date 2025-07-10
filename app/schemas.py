from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr, Field, validator

from .models import InteractionType

class UserBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr
    skills: List[str] = Field(default_list=[], max_length=50)

    @validator("skills")
    def validate_skills(cls, v):
        if not all(isinstance(s, str) for s in v):
            raise ValueError("All skills must be strings")
        if not all(s.strip() for s in v):
            raise ValueError("Skills cannot be empty strings")
        return [s.strip() for s in v]

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

class JobBase(BaseModel):
    title: constr(min_length=1, max_length=200)
    description: constr(min_length=1, max_length=2000)
    required_skills: List[str] = Field(default_list=[], max_length=50)

    @validator("required_skills")
    def validate_required_skills(cls, v):
        if not all(isinstance(s, str) for s in v):
            raise ValueError("All required skills must be strings")
        if not all(s.strip() for s in v):
            raise ValueError("Required skills cannot be empty strings")
        return [s.strip() for s in v]

    class Config:
        from_attributes = True

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

class JobInteractionBase(BaseModel):
    job_id: int = Field(gt=0)
    interaction_type: InteractionType

    class Config:
        from_attributes = True

class JobInteractionCreate(JobInteractionBase):
    pass

class JobInteraction(JobInteractionBase):
    id: int
    user_id: int = Field(gt=0)
    timestamp: datetime

class JobRecommendation(BaseModel):
    job: Job
    match_score: float = Field(ge=0.0, le=1.0)

    class Config:
        from_attributes = True 