from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TELEGRAM_TOKEN')
URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    """Получение нового изображения котика"""
    try:
        response = requests.get(URL).json()
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    """Отправка полученного изображения в чат"""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def say_hi(update, context):
    """Приветствие в ответ на текстовое сообщение"""
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')


def wake_up(update, context):
    """При нажатии /start бот здоровается и отправляет первого котика"""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button
    )
    context.bot.send_photo(chat.id, get_new_image())

# Блок для отправки сообщения
# from telegram import Bot
# chat_id = os.getenv('TELEGRAM_CHAT_ID')
# text = 'Вам телеграмма!'
# bot = Bot(token=secret_token)
# bot.send_message(chat_id, text)


def main():
    """Основная функция"""

    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling(poll_interval=10.0)
    updater.idle()


if __name__ == '__main__':
    main()
