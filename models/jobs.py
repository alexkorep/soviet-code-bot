import yaml
from yaml.loader import SafeLoader
from models.user_status import UserStatusModel


class TechnologyRequirement:
    technology_code: str
    years: int

    def __init__(self, tecnology_dict):
        self.technology_code = tecnology_dict['technology_code']
        self.years = tecnology_dict['years']


class Job:
    code: str
    name: str
    technologies: list
    salary: int
    rating: int
    industry: str
    description: str
    history: str
    city: str
    address: str
    position: str
    technology_requirements: list[TechnologyRequirement]
    responsibilities: str

    def __init__(self, jobdict):
        self.code = jobdict['code']
        self.name = jobdict['name']
        self.technologies = jobdict['technologies']
        self.salary = jobdict['salary']
        self.rating = jobdict['rating']
        self.industry = jobdict['industry']
        self.description = jobdict['description']
        self.history = jobdict['history']
        self.city = jobdict['city']
        self.address = jobdict['address']
        self.position = jobdict['position']

        self.technology_requirements = []
        technology_requirements = jobdict['technology_requirements']
        for tecnology_requirement_dict in technology_requirements:
            self.technology_requirements.append(TechnologyRequirement(tecnology_requirement_dict))

        self.responsibilities = jobdict['responsibilities']


jobs = []

with open('./data/jobs.yaml') as f:
    data = yaml.safe_load(f)
    for rec in data:
        job = Job(rec)
        jobs.append(job)
        # print(job.name, job.technologies, job.salary, job.rating, job.industry, job.description,
        #       job.history, job.city, job.address, job.position, job.requirements, job.responsibilities)


def get_job_score_for_user(job: Job, user_status: UserStatusModel):
    score = 0
    for technology_requirement in job.technology_requirements:
        technology_code = technology_requirement.technology_code
        if technology_code in user_status.technologies:
            score += 1
    return score
