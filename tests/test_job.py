import os
import unittest
from models.job import Job

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'testdata')


class TestJob(unittest.TestCase):

    def test_load_jobs_from_file(self):
        file_path = os.path.join(TEST_DATA_DIR, 'jobs.yaml')
        jobs = Job.load_jobs_from_file(file_path)
        self.assertEqual(len(jobs), 2)
        self.assertEqual(jobs[0].id, 'job1')
        self.assertEqual(jobs[0].company, 'Company A')
        self.assertEqual(jobs[0].title, 'Software Engineer')
        self.assertEqual(jobs[0].description, 'Develop software applications.')
        self.assertEqual(len(jobs[0].required_skills), 2)
        self.assertEqual(jobs[0].required_skills[0].id, 'python')
        self.assertEqual(jobs[0].required_skills[0].months, 12)
        self.assertEqual(jobs[0].required_skills[0].priority, 2)
        self.assertEqual(jobs[0].required_skills[1].id, 'java')
        self.assertEqual(jobs[0].required_skills[1].months, 6)
        self.assertEqual(jobs[0].required_skills[1].priority, 1)
        self.assertEqual(jobs[0].base_probability, 0.8)

        self.assertEqual(jobs[1].id, 'job2')
        self.assertEqual(jobs[1].company, 'Company B')
        self.assertEqual(jobs[1].title, 'Data Scientist')
        self.assertEqual(jobs[1].description, 'Analyze data and build models.')
        self.assertEqual(len(jobs[1].required_skills), 1)
        self.assertEqual(jobs[1].required_skills[0].id, 'python')
        self.assertEqual(jobs[1].required_skills[0].months, 18)
        self.assertEqual(jobs[1].required_skills[0].priority, 3)
        self.assertEqual(jobs[1].base_probability, 0.9)


if __name__ == '__main__':
    unittest.main()
