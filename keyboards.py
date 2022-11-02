from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import service_class

def get_select_category_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for category in service_class.CategoryManager().list():
        keyboard.add(
            InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}')
        )

    return keyboard


def get_default_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(text='Дропни анек', callback_data='drop'),
        InlineKeyboardButton(text='Сменить категорию', callback_data='change_category')
    )

    return keyboard
