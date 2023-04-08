import yaml
from yaml.loader import SafeLoader

jobs = []

with open('./data/jobs.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    jobs = data