import logging
import os
import sys

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiohttp import ClientResponse
from dotenv import load_dotenv

from others import custom_exceptions

load_dotenv()

cat_btn: KeyboardButton = KeyboardButton('Кошка')
dog_btn: KeyboardButton = KeyboardButton('Собака')
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    resize_keyboard=True).add(cat_btn, dog_btn)


def check_token() -> bool:
    return bool(os.getenv('TELEGRAM_TOKEN'))


if not check_token():
    message: str = "Отсутствует токен!"
    logging.critical(message)
    sys.exit(message)
else:
    bot: Bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
    dp: Dispatcher = Dispatcher(bot)


async def get_new_image(animal_type: str) -> str:
    if animal_type not in ('cat', 'dog'):
        raise custom_exceptions.InvalidArgument('Валидные аргументы (cat/dog)')
    try:
        async with aiohttp.ClientSession() as session:
            response_obj: ClientResponse = await session.get(
                f'https://api.the{animal_type}api.com/v1/images/search')
            if response_obj.status != 200:
                raise custom_exceptions.BadCodeStatus('Не успешный код ответа')
    except Exception as _error:
        message: str = 'API не отвечает'
        logging.critical(message, _error, exc_info=True)
        return message

    response_json: dict = await response_obj.json()
    return response_json[0].get('url')


@dp.message_handler(lambda message: message.text == 'Кошка')
async def print_new_cat(message: types.Message):
    await message.answer_photo(await get_new_image('cat'))


@dp.message_handler(lambda message: message.text == 'Собака')
async def print_new_dog(message: types.Message):
    await message.answer_photo(await get_new_image('dog'))


@dp.message_handler(commands=['start'])
async def print_commands(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="""
Чтобы получить фото нажмите кнопку

Автор @Imwisagist""", reply_markup=keyboard)


@dp.message_handler()
async def print_some_help(message: types.Message):
    await message.answer('Чтобы узнать доступные команды нажми /start')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler('log.txt', encoding='utf-8'),
                  logging.StreamHandler(sys.stdout)],
        format="%(name)s %(levelname)s %(funcName)s %(lineno)d %(message)s"
    )
    executor.start_polling(dp, skip_updates=True)
