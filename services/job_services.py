from typing import List, Dict
from models.game_state import SkillLevel
from models.job import Job


def filter_jobs_by_skills(jobs: List[Job], skill_levels: List[SkillLevel]) -> List[Job]:
    """ Return only jobs that has probability > 0. 
        @param jobs: List of jobs to filter
        @param skill_levels: List of skill levels
    """
    filtered_jobs = []
    skill_months_dict = {skill.id: skill.months for skill in skill_levels}
    for job in jobs:
        probability = calculate_job_acceptance_probability(job, skill_months_dict)
        if probability > 0:
            job.acceptance_probability = probability
            filtered_jobs.append(job)
    return filtered_jobs


def calculate_job_acceptance_probability(job: Job, user_skill_months_dict: Dict[str, int]) -> float:
    """Calculate the probability of being accepted for a job."""
    probability = job.base_probability
    for skill in job.required_skills:
        skill_id = skill.id
        months = skill.months
        priority = skill.priority

        if user_skill_months_dict.get(skill_id, 0) < months:
            probability *= 0.9 ** ((months - user_skill_months_dict.get(
                skill_id, 0)) * priority)
        else:
            probability *= 1.05 ** ((user_skill_months_dict.get(skill_id, 0) -
                                    months) / priority)
    return probability
