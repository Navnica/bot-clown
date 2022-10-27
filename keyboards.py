import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_select_category_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    categories = json.load(open('config.json', encoding='utf-8'))['category']
    for category in categories:
        keyboard.add(
            InlineKeyboardButton(text=category, callback_data=category)
        )

    return keyboard


def get_default_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(text='Дропни анек', callback_data='drop'),
        InlineKeyboardButton(text='Сменить категорию', callback_data='change_category')
    )

    return keyboard
