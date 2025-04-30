# test_bot_handlers.py
import pytest
from unittest.mock import patch, MagicMock
from telebot import types
from tg_subscribers.bot_handlers import subscribe, unsubscribe
from tg_subscribers.models import TelegramSubscriber


@pytest.mark.django_db
class TestBotHandlers:
    def test_subscribe_new_user(self):
        """Тестируем подписку нового пользователя"""
        message = MagicMock(spec=types.Message)
        message.chat_id = 12345
        message.reply_to.return_value = None

        with patch('tg_subscribers.models.TelegramSubscriber.objects.get_or_create') as mock_get:
            mock_get.return_value = (MagicMock(), True)
            subscribe(message)

            message.reply_to.assert_called_once_with(message, "✅ Вы подписались на уведомления о входах в админку")
            mock_get.assert_called_once_with(chat_id=12345)

    def test_subscribe_existing_user(self):
        """Тестируем повторную подписку существующего пользователя"""
        message = MagicMock(spec=types.Message)
        message.chat.id = 12345
        message.reply_to.return_value = None

        with patch('tg_subscribers.models.TelegramSubscriber.objects.get_or_create') as mock_get:
            mock_get.return_value = (MagicMock(), False)
            subscribe(message)

            message.reply_to.assert_called_once_with(message, "ℹ️ Вы уже подписаны на уведомления")

    def test_unsubscribe_subscribed_user(self):
        """Тестируем отписку подписанного пользователя"""
        message = MagicMock(spec=types.Message)
        message.chat.id = 12345
        message.reply_to.return_value = None

        TelegramSubscriber.objects.create(chat_id=12345)

        unsubscribe(message)

        message.reply_to.assert_called_once_with(message, "❌ Вы отписались от уведомлений")
        assert not TelegramSubscriber.objects.filter(chat_id=12345).exists()

    def test_unsubscribe_non_subscribed_user(self):
        """Тестируем отписку неподписанного пользователя"""
        message = MagicMock(spec=types.Message)
        message.chat.id = 12345
        message.reply_to.return_value = None

        unsubscribe(message)

        message.reply_to.assert_called_once_with(message, "ℹ️ Вы не были подписаны на уведомления")