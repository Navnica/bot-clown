import json


class UserWorker:
    def __init__(self, user_id) -> None:
        self.user_id: str = str(user_id)
        self.users: dict = json.load(open('users.json', encoding='utf-8'))

    def user_registered(self) -> bool:
        return self.user_id in self.users

    def get_message_id(self) -> int:
        return self.users[self.user_id]['message_id']

    def get_category(self) -> str:
        return self.users[self.user_id]['category']

    def register_user(self) -> None:
        self.users[self.user_id] = {}
        self.dump_updates()

    def set_user_category(self, category) -> None:
        self.users[self.user_id]['category'] = category
        self.dump_updates()

    def set_user_message(self, message_id) -> None:
        self.users[self.user_id]['message_id'] = message_id
        self.dump_updates()

    def dump_updates(self) -> None:
        json.dump(self.users, open('users.json', 'w', encoding='utf-8'))
