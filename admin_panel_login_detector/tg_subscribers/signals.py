from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from .models import TelegramSubscriber
from .services import bot


@receiver(user_logged_in)
def send_login_notification(sender, request, user, **kwargs):
    print(33333)
    if request.path.startswith('/admin/'):
        # Формируем сообщение
        login_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"🔔 Новый вход в админку:\nДата: {login_time}\nПользователь: {user.username}"

        # Отправляем сообщение всем подписчикам
        subscribers = TelegramSubscriber.objects.all()
        for subscriber in subscribers:
            try:
                bot.send_message(subscriber.chat_id, message)
            except Exception as e:
                print(f"Failed to send message to {subscriber.chat_id}: {e}")
