import datetime
from marshmallow import Schema, fields, post_load, ValidationError
from typing import List, Union
from project_utils import setup_logging
log = setup_logging('current_log')
from project_utils import get_user_id


class UserSignUp(object):
    def __init__(self, username: str, email: str, password: str, first_name: str, last_name: str, gender: str,
                 phone_no: int):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_no = phone_no
        self.created_on = datetime.datetime.utcnow()
        self.user_id = get_user_id()

    @staticmethod
    def load_from_json(json_str: Union[dict]) -> (object, str):
        schema = UserSignUpSchema()
        try:
            return schema.load(json_str), ''
        except ValidationError as ex:
            log.exception(ex)
            return None, f'Could not parse request. Reason: {ex.messages}'
        except Exception as ex:
            log.exception(ex)
            return None, 'Could not parse request.'


class UserSignUpSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    gender = fields.Str(required=True)
    phone_no = fields.Int(required=True)

    @post_load
    def make_model(self, data, **kwargs):
        return UserSignUp(**data)
