# tt_django_login_detector

## Описание
Приложение, регистрирующее все входы в Django админ панель 
и отправляющее сообщение всем пользователям-подписчикам заданного Telegram-бота

## Переменные окружения
Перед запуском нужно создать файл `.env` в `admin_panel_login_detector_project/` с переменной \
`TELEGRAM_BOT_TOKEN=` - токен бота, который можно получить у @BotFather

## Команды бота
`/subscribe` - пользователь пытается подписаться на бота
`/unsubscribe` - пользователь пытается отписаться от бота

## Требования
**pyenv** - для запуска через **CMD** \
**Docker**  - для запуска  в Docker) 

## Запуск в Docker
```commandline
docker build --progress=plain  -t admin_panel . && \
docker run -it  -p 8000:8000 admin_panel
```
Сайт будет поднят и доступен по адресу`http://127.0.0.1:8000/admin/` \
По умолчанию в админке будет логин - `admin`, пароль - `admin`  

## Запуск в CMD

### Установка зависимостей
`pyenv local 3.12.4` \
`python -m venv .venv` \
`source ./.venv/bin/activate` \
`pippip install -r requirements.txt` 

### Запуск
`python manage.py migrate`\
`python manage.py createsuperuser`\
`python manage.py runserver`


