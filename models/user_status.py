from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, JSONAttribute

TABLE_NAME = 'soviet_code_bot_user_status'

DEFAULT_STATUS = {
    'current_month': 0,
    'job_history': [],
}

class UserStatusModel(Model):
    class Meta:
        table_name = TABLE_NAME
    chat_dest = NumberAttribute(hash_key=True)
    current_month = NumberAttribute(null=True)
    job_history = JSONAttribute(null=True)
    technologies = JSONAttribute(null=True)
