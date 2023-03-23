# Animal bot

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)

Асинхронный бот для любителей посозерцать животных, на борту имеет 2 кнопки,
в зависимости от нажатой кнопки возвращает в тг чат фото кошки или собаки =)

## Автор

- :white_check_mark: [Imwisagist](https://github.com/Imwisagist)

# Подготовка и запуск проекта в 5 шагов локально или в 1 шаг докером
## Локально:
### 1)Склонировать репозиторий на локальную машину:
```
git clone https://github.com/Imwisagist/Animal_bot.git
```
### 2)Необходим токен:
* Токен бота берётся у BotFather'a в ТГ:
```
cd Animal_bot/
nano .env
TELEGRAM_TOKEN=<Токен Вашего бота>
```
### 3)Создайте виртуальное окружение, обновите пакетный менеджери установите зависимости:
```
python -m venv venv && source venv/scripts/activate &&
python -m pip install --upgrade pip && pip install -r requirements.txt
```
### 4)Запустите:
```
python animalbot.py
```
### 5)Напишите своему боту в лс:
```
или моему(не гарантирую что он будет доступен:))
https://t.me/wisagist_kittybot
или
@wisagist_kittybot
```
## Докером:
### 1)Запустите докером с токеном:
```
docker run --rm -e TELEGRAM_TOKEN=<Токен_Вашего_бота> imwisagist/animalbot:v1.0
```
# Примеры ответов:
### Получить все доступные команды: /start
* Ответ на запрос: /start
```
Чтобы получить фото нажмите кнопку

Автор @imwisagist

     Кнопки:
Кошка       Собака
```
* Ответ на запрос: <любой текст>
```
Чтобы узнать доступные команды нажми /start
```
* Ответ при нажатии на кнопку Кошка - Фото кошки
![cat_image](https://github.com/imwisagist/Animal_bot/blob/main/cat.jpg?raw=true)
* Ответ при нажатии на кнопку Собака - Фото собаки
![dog_image](https://github.com/imwisagist/Animal_bot/blob/main/dog.jpg?raw=true)