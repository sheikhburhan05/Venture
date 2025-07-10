from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
import enum
from typing import List

from .database import Base

class InteractionType(str, enum.Enum):
    VIEW = "view"
    APPLY = "apply"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    _skills = Column("skills", String)

    interactions = relationship("JobInteraction", back_populates="user")

    @property
    def skills(self) -> List[str]:
        return self._skills.split(",") if self._skills else []

    @skills.setter
    def skills(self, value: List[str]):
        if not isinstance(value, list):
            raise ValueError("Skills must be a list of strings")
        self._skills = ",".join(value) if value else ""

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    _required_skills = Column("required_skills", String)

    interactions = relationship("JobInteraction", back_populates="job")

    @property
    def required_skills(self) -> List[str]:
        return self._required_skills.split(",") if self._required_skills else []

    @required_skills.setter
    def required_skills(self, value: List[str]):
        if not isinstance(value, list):
            raise ValueError("Required skills must be a list of strings")
        self._required_skills = ",".join(value) if value else ""

class JobInteraction(Base):
    __tablename__ = "job_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    interaction_type = Column(SQLEnum(InteractionType))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="interactions")
    job = relationship("Job", back_populates="interactions") 