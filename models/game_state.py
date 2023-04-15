from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    MapAttribute,
    NumberAttribute,
    ListAttribute,
)


TABLE_NAME = 'soviet_code_bot_game_state'

class SkillLevel(MapAttribute):
    id = UnicodeAttribute()
    level = NumberAttribute()

class GameState(Model):
    class Meta:
        table_name = TABLE_NAME

    user_id = NumberAttribute(hash_key=True)
    current_date = UnicodeAttribute()
    skill_levels = ListAttribute(of=SkillLevel)
    job_history = ListAttribute()

    @staticmethod
    def load_from_dynamodb(user_id):
        try:
            print('user_id', user_id)
            return GameState.get(user_id)
        except GameState.DoesNotExist:
            return GameState(user_id=user_id)

    def save_to_dynamodb(self):
        self.save()
