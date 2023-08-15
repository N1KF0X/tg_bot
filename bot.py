import telebot
from telebot import types


bot = telebot.TeleBot('6302035714:AAFy_PwoNsduOyMU5UH5uP51fOh7Jew31SA')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ink_button = types.KeyboardButton('Прибавить к числу 1')
    link_button = types.KeyboardButton('Перейти к репозиторию')
    markup.add(ink_button, link_button)
    bot.send_message(message.from_user.id, 'Тестовый бот работает', reply_markup=markup)


bot.infinity_polling()