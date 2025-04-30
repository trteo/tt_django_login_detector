# bot_handlers.py
import telebot
from .models import TelegramSubscriber
from .services import bot


# bot = telebot.TeleBot('7798934875:AAEO-NsK5wiG2n_Yjvnlmr1SkNGnaXs3JaE')


@bot.message_handler(commands=['start'])
def subscribe(message):
    print(1421336451)
    chat_id = message.chat.id
    subscriber, created = TelegramSubscriber.objects.get_or_create(chat_id=chat_id)
    if created:
        bot.reply_to(message, "✅ Вы подписались на уведомления о входах в админку")
    else:
        bot.reply_to(message, "ℹ️ Вы уже подписаны на уведомления")


@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    print(97898987)
    chat_id = message.chat.id
    deleted, _ = TelegramSubscriber.objects.filter(chat_id=chat_id).delete()
    if deleted:
        bot.reply_to(message, "❌ Вы отписались от уведомлений")
    else:
        bot.reply_to(message, "ℹ️ Вы не были подписаны на уведомления")
