import json


def user_registered(user_id: str) -> bool:
    return str(user_id) in json.load(open('users.json', encoding='utf-8'))


def register_user(user: dict) -> None:
    users: dict = json.load(open('users.json', encoding='utf-8'))
    users[str(user['id'])] = {}
    json.dump(users, open('users.json', 'w', encoding='utf-8'))


def set_user_category(user_id: str, category: str) -> None:
    users: dict = json.load(open('users.json', encoding='utf-8'))
    users[str(user_id)]['category'] = category
    json.dump(
        users,
        open('users.json', 'w', encoding='utf-8')
    )


def set_user_message(user_id: str, message_id: str) -> None:
    users: dict = json.load(open('users.json', encoding='utf-8'))
    users[str(user_id)]['message_id'] = str(message_id)
    json.dump(
        users,
        open('users.json', 'w')
    )
