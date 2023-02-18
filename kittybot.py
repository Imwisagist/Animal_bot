from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TELEGRAM_TOKEN')
URL_CAT = 'https://api.thecatapi.com/v1/images/search'
URL_DOG = 'https://api.thedogapi.com/v1/images/search'


def get_new_image(who):
    """Получение нового изображения котика/пёсика"""
    try:
        response = requests.get(who).json()
    except Exception as error:
        print(error)
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    random_animal = response[0].get('url')
    return random_animal


def new(update, context):
    """Отправка полученного изображения в чат"""
    chat = update.effective_chat
    its_dog_or_cat = update.effective_message.text
    context.bot.send_photo(chat.id, get_new_image(
                           URL_CAT if its_dog_or_cat == "/newcat" else URL_DOG))


def say_hi(update, context):
    """Приветствие в ответ на текстовое сообщение"""
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyDoggyBot!')


def wake_up(update, context):
    """При нажатии /start бот здоровается и отправляет первого котика"""
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/newcat'], ['/newdog']], resize_keyboard=True)
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл'.format(name),
        reply_markup=button,
    )
    context.bot.send_photo(chat.id, get_new_image(URL_CAT))


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new))
    updater.dispatcher.add_handler(CommandHandler('newdog', new))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
    updater.start_polling(poll_interval=10.0)
    updater.idle()


if __name__ == '__main__':
    main()
