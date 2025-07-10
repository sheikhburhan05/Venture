from sqlalchemy.orm import Session
from typing import List, Dict, Set
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..models import User, Job, JobInteraction, InteractionType
from ..schemas import JobRecommendation

def get_previously_applied_skills(db: Session, user_id: int) -> Set[str]:
    try:
        applied_jobs = (
            db.query(Job)
            .join(JobInteraction)
            .filter(
                JobInteraction.user_id == user_id,
                JobInteraction.interaction_type == InteractionType.APPLY
            )
            .all()
        )
        
        applied_skills = set()
        for job in applied_jobs:
            applied_skills.update(skill.lower() for skill in job.required_skills)
        
        return applied_skills
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching applied skills: {str(e)}"
        )

def calculate_weighted_match_score(
    user_skills: List[str],
    job_skills: List[str],
    previously_applied_skills: Set[str],
    skill_weight: float = 2.0
) -> float:
    try:
        if not user_skills or not job_skills:
            return 0.0
        
        user_skills_set = set(s.lower() for s in user_skills)
        job_skills_set = set(s.lower() for s in job_skills)
        matching_skills = user_skills_set.intersection(job_skills_set)
        
        score = 0.0
        total_weight = 0.0
        
        for skill in job_skills_set:
            skill_lower = skill.lower()
            if skill_lower in matching_skills:
                weight = skill_weight if skill_lower in previously_applied_skills else 1.0
                score += weight
            total_weight += skill_weight if skill_lower in previously_applied_skills else 1.0
        
        return score / total_weight if total_weight > 0 else 0.0
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating match score: {str(e)}"
        )

def get_recommendations(db: Session, user_id: int) -> List[JobRecommendation]:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        jobs = db.query(Job).all()
        if not jobs:
            return []
        
        previously_applied_skills = get_previously_applied_skills(db, user_id)
        recommendations = []
        
        for job in jobs:
            match_score = calculate_weighted_match_score(
                user.skills,
                job.required_skills,
                previously_applied_skills
            )
            recommendations.append({
                "job": job,
                "match_score": match_score
            })
        
        recommendations.sort(key=lambda x: x["match_score"], reverse=True)
        return recommendations[:3]
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching recommendations: {str(e)}"
        ) 