from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import service_class


def get_select_category_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    for category in service_class.CategoryManager().list():
        keyboard.add(
            InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}')
        )

    return keyboard


def get_default_markup(joke) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton(text='Дропни анек', callback_data='drop'),
        InlineKeyboardButton(text='Сменить категорию', callback_data='change_category'),
        InlineKeyboardButton(text=f'👍 {joke.rate_plus if joke.rate_plus != 0 else ""}',
                             callback_data=f'rate_plus_{joke.id}'),
        InlineKeyboardButton(text=f'👎 {joke.rate_minus if joke.rate_minus != 0 else ""}',
                             callback_data=f'rate_minus_{joke.id}'),
        InlineKeyboardButton(text='Добавить анекдот', callback_data='add_user_joke')
    )

    return keyboard


def get_markup_back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton(text='<', callback_data='back')]])
