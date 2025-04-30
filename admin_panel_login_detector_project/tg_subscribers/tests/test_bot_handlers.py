import pytest
from unittest.mock import patch, MagicMock
from telebot import types
from tg_subscribers.bot_handlers import subscribe, unsubscribe
from tg_subscribers.models import TelegramSubscriber


@pytest.mark.django_db
class TestBotHandlers:
    def test_subscribe_new_user(self):
        """Тестируем подписку нового пользователя"""
        chat = MagicMock(spec=types.Chat)
        chat.id = 12345
        message = MagicMock(spec=types.Message)
        message.chat = chat
        message.message_id = 1111

        with patch('tg_subscribers.models.TelegramSubscriber.objects.get_or_create') as mock_get, \
                patch('tg_subscribers.services.bot.reply_to') as mock_reply_to:
            mock_get.return_value = (MagicMock(), True)
            subscribe(message)

            mock_reply_to.assert_called_once_with(message, "✅ Вы подписались на уведомления о входах в админку")
            mock_get.assert_called_once_with(chat_id=12345)
