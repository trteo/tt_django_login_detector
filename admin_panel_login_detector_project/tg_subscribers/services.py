import telebot

from admin_panel_login_detector import settings

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)