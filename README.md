# tt_django_login_detector

## Описание
Приложение, регистрирующее все входы в Django админ панель 
и отправляющее сообщение всем пользователям-подписчикам заданного Telegram-бота

## Переменные окружения
Нужно создать файл в `admin_panel_login_detector_project/.env` с переменной \
`TELEGRAM_BOT_TOKEN=` - токен бота, который можно получить у @BotFather

## Команды бота
`/subscribe` - пользователь пытается подписаться на бота
`/unsubscribe` - пользователь пытается отписаться от бота

## Требования
**pyenv** - для запуска через **CMD**
**Docker**

## Запуск в Docker


## Запуск в CMD

## Установка зависимостей
`pyenv local 3.12.4` \
`python -m venv .venv` \
`source ./.venv/bin/activate` \
`pippip install -r requirements.txt` 

## Запуск
`python manage.py migrate`
`python manage.py createsuperuser`
`python manage.py runserver`


