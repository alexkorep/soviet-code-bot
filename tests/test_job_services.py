import unittest
from models.job import Job, RequiredSkill
from models.game_state import SkillLevel
from services.job_services import filter_jobs_by_skills, calculate_job_acceptance_probability

COMPANY = 'Google'
TITLE = 'Software Engineer'
DESCRIPTION = 'Build the next generation of Google products.'


class TestJobFilter(unittest.TestCase):
    def setUp(self):
        self.jobs = [
            Job('Software Engineer', COMPANY, TITLE, DESCRIPTION, [
                RequiredSkill('Python', 3, 1),
                RequiredSkill('Django', 2, 1),
                RequiredSkill('SQL', 1, 1)
            ], 0.5),
            Job('Data Analyst', COMPANY, TITLE, DESCRIPTION, [
                RequiredSkill('Python', 2, 1),
                RequiredSkill('SQL', 3, 1)
            ], 0.3),
            Job('DevOps Engineer', COMPANY, TITLE, DESCRIPTION, [
                RequiredSkill('Docker', 2, 1),
                RequiredSkill('AWS', 1, 1)
            ], 0.4)
        ]
        self.user_skill_months = [
            SkillLevel(id='Python', months=3),
            SkillLevel(id='Django', months=2),
        ]

    def test_filter_jobs_by_skills(self):
        filtered_jobs = filter_jobs_by_skills(
            self.jobs, self.user_skill_months)
        self.assertEqual(len(filtered_jobs), 3)
        self.assertIn(self.jobs[0], filtered_jobs)
        self.assertIn(self.jobs[1], filtered_jobs)
        self.assertIn(self.jobs[2], filtered_jobs)

    def test_calculate_job_acceptance_probability(self):
        job = Job('Software Engineer', COMPANY, TITLE, DESCRIPTION, [
            RequiredSkill('Python', 3, 1),
            RequiredSkill('Django', 2, 1),
            RequiredSkill('SQL', 1, 1)
        ], 0.5)
        probability = calculate_job_acceptance_probability(
            job, self.user_skill_months)
        self.assertAlmostEqual(probability, 0.45, places=3)
