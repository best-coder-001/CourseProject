import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR.joinpath("assets", "data")


class UserModel:
    def __init__(self):
        self.path_to_data = Path.joinpath(
            DATA_DIR, 'users.json'
        )

    def append_user(self, **kw):
        with open(f'{self.path_to_data}', 'r') as file:
            users = json.load(file)

        users['users'].append(kw)

        with open(self.path_to_data, 'w') as file:
            json.dump(users, file)

    def check_logged(self, **kw):
        users = self.read_users_json()

        for user in users['users']:
            if user['username'] == kw['username'] and user['password'] == kw['password']:
                return True
            else:
                return False

    def read_users_json(self):
        with open(f'{self.path_to_data}', 'r') as file:
            users = json.load(file)
            return users

    def validate_user_data(self):
        pass
