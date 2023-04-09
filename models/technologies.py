import yaml

technologies = []

with open('./data/technologies.yaml') as f:
    technologies = yaml.safe_load(f)

def get_technology_by_code(code):
    for tech in technologies:
        if tech['code'] == code:
            return tech
    return None