from typing import List

def string_to_list(string: str) -> List[str]:
    """Convert comma-separated string to list of strings."""
    return [s.strip() for s in string.split(',') if s.strip()]

def list_to_string(lst: List[str]) -> str:
    """Convert list of strings to comma-separated string."""
    return ','.join(lst)

def calculate_match_score(user_skills: List[str], job_skills: List[str]) -> float:
    """Calculate the match score between user skills and job required skills."""
    if not user_skills or not job_skills:
        return 0.0
    
    user_skills_set = set(s.lower() for s in user_skills)
    job_skills_set = set(s.lower() for s in job_skills)
    
    matching_skills = len(user_skills_set.intersection(job_skills_set))
    total_required_skills = len(job_skills_set)
    
    return matching_skills / total_required_skills if total_required_skills > 0 else 0.0 