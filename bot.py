import json
import random
import telebot
import userworker
import keyboards
import anekmanage
import cowsay

config = json.load(open('config.json', encoding='utf-8'))
bot = telebot.TeleBot(config['token'])


@bot.message_handler(content_types=['text'])
def get_text_messages(message) -> None:
    user_worker = userworker.UserWorker(message.from_user.id)
    if not user_worker.user_registered():
        user_worker.register_user()

    bot.send_message(chat_id=message.from_user.id, text='👉👈🥺', reply_markup=keyboards.get_select_category_markup())
    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{message.from_user.id} : {message.text}'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    user_worker = userworker.UserWorker(call.from_user.id)
    user_worker.set_user_message(call.message.id)

    if call.data == 'change_category':
        bot.edit_message_text(chat_id=call.from_user.id, text='🫵🏻🤡', message_id=user_worker.get_message_id(),
                              reply_markup=keyboards.get_select_category_markup())

    if call.data in config['category']:
        user_worker.set_user_category(category=call.data)
        bot.edit_message_text(text='👉👈🥺', chat_id=call.from_user.id, message_id=user_worker.get_message_id(),
                              reply_markup=keyboards.get_default_markup())

    if call.data == 'drop':
        anek = anekmanage.get_anek_with_category(user_worker.get_category())
        bot.edit_message_text(text=anek, chat_id=call.from_user.id, message_id=user_worker.get_message_id(),
                              reply_markup=keyboards.get_default_markup())

    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{call.from_user.id} : {call.data}'))


def start_polling():
    bot.infinity_polling()
