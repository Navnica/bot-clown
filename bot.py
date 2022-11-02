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
    user_manager = service_class.UserManager(call.from_user.id)
    user_manager.set_message(call.message.id)

    if call.data == 'change_category':
        bot.edit_message_text(chat_id=call.from_user.id, text='🫵🏻🤡', message_id=user_worker.get_message_id(),
                              reply_markup=keyboards.get_select_category_markup())

    if 'category_' in call.data:
        category_id = service_class.CategoryManager(int(call.data.replace('category_', ''))).get()
        user_manager.set_category(category_id)
        bot.edit_message_text(text='👉👈🥺', chat_id=call.from_user.id, message_id=user_manager.get().get_message_id(),
                              reply_markup=keyboards.get_default_markup())

    if call.data == 'drop':
        anek = anekmanage.get_anek_with_category(user_worker.get_category())
        bot.edit_message_text(text=anek, chat_id=call.from_user.id, message_id=user_worker.get_message_id(),
                              reply_markup=keyboards.get_default_markup())

    print(cowsay.get_output_string(random.choice(cowsay.char_names), f'{call.from_user.id} : {call.data}'))


def start_polling():
    bot.infinity_polling()
