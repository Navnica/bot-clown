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
def get_text_messages(message):
    if not userworker.user_registered(message.from_user.id):
        userworker.register_user(message.from_user.__dict__)

    bot.send_message(chat_id=message.from_user.id, text='👉👈🥺', reply_markup=keyboards.get_select_category_markup())
    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{message.from_user.id} : {message.text}'))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    userworker.set_user_message(call.from_user.id, call.message.id)
    user = json.load(open('users.json', encoding='utf-8'))[str(call.from_user.id)]

    if call.data == 'change_category':
        bot.edit_message_text(chat_id=call.from_user.id, text='🫵🏻🤡', message_id=user['message_id'],
                              reply_markup=keyboards.get_select_category_markup())

    if call.data in config['category']:
        userworker.set_user_category(user_id=call.from_user.id, category=call.data)
        bot.edit_message_text(text='👉👈🥺', chat_id=call.from_user.id, message_id=user['message_id'],
                              reply_markup=keyboards.get_default_markup())

    if call.data == 'drop':
        anek = anekmanage.get_anek_with_category(user['category'])
        bot.edit_message_text(text=anek, chat_id=call.from_user.id, message_id=user['message_id'],
                              reply_markup=keyboards.get_default_markup())

    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{call.from_user.id} : {call.data}'))

def start_polling():
    bot.infinity_polling()
