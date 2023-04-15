import yaml
import unittest
from os import path

from schema import Schema, And, Optional, Use

REQUIRED_SKILL_SCHEMA = Schema({
    'id': And(str, len),
    'months': And(int, lambda x: x > 0),
    'priority': And(float, lambda x: 0 <= x <= 1)
})

JOB_SCHEMA = Schema({
    'id': And(str, len),
    'company': str,
    'title': str,
    'description': str,
    'required_skills': And([REQUIRED_SKILL_SCHEMA]),
    'base_probability': And(float, lambda x: 0 <= x <= 1)
})

JOBS_SCHEMA = Schema([JOB_SCHEMA])


def validate_jobs_file(file_path: str) -> bool:
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    try:
        JOBS_SCHEMA.validate(data)
        return True
    except Exception:
        return False


class TestValidateJob(unittest.TestCase):

    def test_valid_file(self):
        # Get the path to the ../data/jobs.yaml file
        file_path = path.join(path.dirname(__file__),
                              '..', 'data', 'jobs.yaml')
        self.assertTrue(validate_jobs_file(file_path))
