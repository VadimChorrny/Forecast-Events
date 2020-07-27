# підключаю рандом
import random

# Підключаю телеграм модуль

import telebot

# сюда вводим токен

bot = telebot.TeleBot('963264448:AAGVbz1rtI4F1rJnBOGq4ceo17yGoG7q5og')

# імпортую типи модуля щоб добавить кнопкі

from telebot import types

# В цьому рандомі буде зберігатися відповідь коли буду тиснути на кнопкі
rand = ["Я думаю краще тобі сюда не йти!","Навіщо тобі ті пари","ДУМАЙ!","Сьогодні інфа100, буде легка пара","Сьогодні точно потрібно йти на пару!","А якщо там будуть ставить халявні кристали?"]

# Ця штука отримує і опрацьовує повідомлення

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Якщо написати Привіт

    if message.text == "!Пара":

        # Вітаємся :))

        bot.send_message(message.from_user.id, "Привіт, хочеш розкажу, що буде сьогодні на парі?")

        # Тепер добавляю кнопкі

        keyboard = types.InlineKeyboardMarkup()

        # Тепер добавляєм для кожної пари

        key_infa = types.InlineKeyboardButton(text='Адмінка', callback_data='para')

        # а ця маленька хрень добавляє саму кнопку

        keyboard.add(key_infa)

        key_math = types.InlineKeyboardButton(text='Програмування', callback_data='para')

        keyboard.add(key_math)

        # тепер показуєм всі кнопкі і просим вибрать пару

        bot.send_message(message.from_user.id, text='Вибери свою пару:', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Якщо не розумієш, що тут за двіж просто напиши Привіт")

    else:
        bot.send_message(message.from_user.id, "Жалко, що мій володарь Вадим Чорний не навчив мене говорити, якщо щось не розумієш напиши /help")

        bot.send_message(message.from_user.id, "А якшо тобі не цікаво тоді вали звідси !!!")    # кста тепер можна добавлять багато меседжів :)
# це обробляє натиски на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "para":
        # Формуєм предвгадування
        msg = random.choice(rand)
        # Відправляєм текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# постійний запит боту
bot.polling(none_stop=True, interval=0)