import json
import random
import telebot
import keyboards
import cowsay
import service_class


config = json.load(open('config.json', encoding='utf-8'))
bot = telebot.TeleBot(config['token'])


@bot.message_handler(content_types=['text'])
def get_text_messages(message) -> None:
    user_manager = service_class.UserManager(message.from_user.id)

    if user_manager.get() is None:
        user_manager.add()

    bot.send_message(
        chat_id=message.from_user.id,
        text='👉👈🥺',
        reply_markup=keyboards.get_select_category_markup())

    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{message.from_user.id} : {message.text}'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{call.from_user.id} : {call.data}'))

    user_manager = service_class.UserManager(call.from_user.id)
    user_manager.set_message(call.message.id)

    if call.data == 'change_category':
        bot.edit_message_text(
            chat_id=call.from_user.id,
            text='🫵🏻🤡',
            message_id=user_manager.get().message_id,
            reply_markup=keyboards.get_select_category_markup())

    if 'category_' in call.data:
        category_id = service_class.CategoryManager(int(call.data.replace('category_', ''))).get()
        user_manager.set_category(category_id)
        call.data = 'drop'

    if call.data == 'drop':
        random_joke = service_class.CategoryManager(user_manager.get().category).random_joke()
        bot.edit_message_text(
            text=random_joke.text,
            chat_id=call.from_user.id,
            message_id=user_manager.get().message_id,
            reply_markup=keyboards.get_default_markup(random_joke))

    if call.data.startswith('rate_plus') or call.data.startswith('rate_minus'):
        rate_plus = call.data.startswith('rate_plus')
        joke = service_class.JokeManager(int(call.data.replace('rate_plus_' if rate_plus else 'rate_minus_', ''))).get()

        if service_class.RateManager().add(user_id=call.from_user.id, joke_id=joke.id, rate_plus=rate_plus) == 0:
            return

        bot.edit_message_text(
            text=joke.text,
            chat_id=call.from_user.id,
            message_id=user_manager.get().message_id,
            reply_markup=keyboards.get_default_markup(service_class.JokeManager(joke_id=joke.id).get()))


def start_polling():
    bot.infinity_polling()
