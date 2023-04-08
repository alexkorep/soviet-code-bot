import yaml
from yaml.loader import SafeLoader

tools = []

with open('./data/tools.yaml') as f:
    tools = yaml.load(f, Loader=SafeLoader)
