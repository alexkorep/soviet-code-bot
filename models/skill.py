import yaml

class Skill:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def load_skills_from_file(file_path):
        with open(file_path, 'r') as f:
            skills_data = yaml.load(f, Loader=yaml.FullLoader)
        skills = []
        for skill_data in skills_data:
            skill = Skill(
                id=skill_data['id'],
                name=skill_data['name'],
                description=skill_data['description'],
            )
            skills.append(skill)
        return skills
