from models.jobs import jobs, Job
from models.technologies import get_technology_by_code
from models.user_status import UserStatusModel


def get_company(code):
    for job in jobs:
        if job.code == code:
            return job
    return None

# def get_technology(code):
#     for job in jobs:
#         for tech in job.technology_requirements:
#             if tech.technology_code == code:
#                 return tech
#     return None

def get_job_score_for_user(job: Job, user_status: UserStatusModel):
    score = 0
    for technology_requirement in job.technology_requirements:
        technology_code = technology_requirement.technology_code
        if technology_code in user_status.technologies:
            score += 1
    return score


def get_experience_dict(user_status: UserStatusModel):
    month = user_status.current_month
    result = {}
    history = user_status.job_history or []
    for job in history[::-1]:
        months_on_job = month - job['start']
        company_code = job['company_code']
        company = get_company(company_code)
        technologies = company.technologies
        if technologies:
            for tech in technologies:
                tech_months = result.get(tech, 0)
                tech_months += months_on_job
                result[tech] = tech_months
        month = job['start']
    return result

def get_experience(user_status: UserStatusModel):
    exp_dict = get_experience_dict(user_status)
    exp = []
    for tech, months in exp_dict.items():
        tech = get_technology_by_code(tech)
        tech['months'] = months
        print('tech', tech)
        exp.append(tech)
    return exp
