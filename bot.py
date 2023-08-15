import telebot
from telebot import types


bot = telebot.TeleBot('6302035714:AAFy_PwoNsduOyMU5UH5uP51fOh7Jew31SA')
is_inc = False

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ink_button = types.KeyboardButton('Икрементировать')
    link_button = types.KeyboardButton('Репозиторий')

    global is_inc
    is_inc = False

    markup.add(ink_button, link_button)
    bot.send_message(message.from_user.id, 'Тестовый бот работает', reply_markup=markup)


@bot.message_handler(commands = ['link'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Ссылка', url='https://github.com/N1KF0X/tg_bot')

    global is_inc
    is_inc = False

    markup.add(button)
    bot.send_message(message.from_user.id, "Перейти", reply_markup = markup)


@bot.message_handler(commands = ['inc'])
def inc(message):
    global is_inc
    is_inc= True

    bot.send_message(message.from_user.id, "Напишите число которое желаете увеличить на 1")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global is_inc

    if message.text == 'Репозиторий':
        url(message)
    elif message.text == 'Икрементировать':
        inc(message)
    elif is_inc:
        try:
            i = int(message.text)
            bot.send_message(message.from_user.id, i+1)
            is_inc= False
        except:
            bot.send_message(message.from_user.id, "Вы ввели не корректное число, повторите попытку")
    else:
        bot.send_message(message.from_user.id, "Не понял")


bot.infinity_polling()