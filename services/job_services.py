from typing import List, Dict
from models.job import Job


def filter_jobs_by_skills(jobs: List[Job], skill_levels: Dict[str, int]) -> List[Job]:
    """ Return only jobs that has probability > 0. 
        @param jobs: List of jobs to filter
        @param skill_levels: Dictionary of skill levels in format {skill_id: level}
    """
    filtered_jobs = []
    for job in jobs:
        probability = calculate_job_acceptance_probability(job, skill_levels)
        if probability > 0:
            job.acceptance_probability = probability
            filtered_jobs.append(job)
    return filtered_jobs


def calculate_job_acceptance_probability(job: Job, skill_levels: Dict[str, int]) -> float:
    """Calculate the probability of being accepted for a job."""
    probability = job.base_probability
    # Iterage through job.required_skills dictionary: {skill_id: level}
    for skill in job.required_skills:
        skill_id = skill.id
        level = skill.level
        priority = skill.priority

        if skill_levels.get(skill_id, 0) < level:
            probability *= 0.9 ** ((level - skill_levels.get(
                skill_id, 0)) * priority)
        else:
            probability *= 1.05 ** ((skill_levels.get(skill_id, 0) -
                                    level) / priority)
    return probability
