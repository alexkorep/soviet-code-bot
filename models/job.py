import yaml
from typing import List


class RequiredSkill:
    def __init__(self, id, level, priority):
        self.id = id
        self.level = level
        self.priority = priority


class Job:
    id: str
    company: str
    title: str
    description: str
    required_skills: List[RequiredSkill]
    base_probability: float

    def __init__(self, id, company, title, description, required_skills, base_probability):
        self.id = id
        self.company = company
        self.title = title
        self.description = description
        self.required_skills = required_skills
        self.base_probability = base_probability

    @staticmethod
    def load_jobs_from_file(file_path):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        jobs = []
        for job_data in data:
            required_skills = [
                RequiredSkill(
                    skill_data['id'], skill_data['level'], skill_data['priority'])
                for skill_data in job_data['required_skills']
            ]
            job = Job(job_data['id'], job_data['company'], job_data['title'], job_data['description'],
                      required_skills, job_data['base_probability'])
            jobs.append(job)
        return jobs
