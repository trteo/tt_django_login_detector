import pytest
from unittest.mock import patch, MagicMock
from telebot import types
from tg_subscribers.bot_handlers import subscribe, unsubscribe
from tg_subscribers.models import TelegramSubscriber
from tg_subscribers.tests.mocks import get_mock_tg_message, CHAT_DEFAULT_ID


@pytest.mark.django_db
class TestBotHandlers:
    def test_subscribe_new_user(self):
        """Тестируем подписку нового пользователя"""
        message = get_mock_tg_message()

        with patch('tg_subscribers.models.TelegramSubscriber.objects.get_or_create') as mock_get, \
                patch('tg_subscribers.services.bot.reply_to') as mock_reply_to:
            mock_get.return_value = (MagicMock(), True)
            subscribe(message)

            mock_reply_to.assert_called_once_with(message, "✅ Вы подписались на уведомления о входах в админку")
            mock_get.assert_called_once_with(chat_id=CHAT_DEFAULT_ID)

    def test_subscribe_existing_user(self):
        """Тестируем повторную подписку существующего пользователя"""
        message = get_mock_tg_message()

        with patch('tg_subscribers.models.TelegramSubscriber.objects.get_or_create') as mock_get, \
                patch('tg_subscribers.services.bot.reply_to') as mock_reply_to:
            mock_get.return_value = (MagicMock(), False)
            subscribe(message)

            mock_reply_to.assert_called_once_with(message, "ℹ️ Вы уже подписаны на уведомления")
            mock_get.assert_called_once_with(chat_id=CHAT_DEFAULT_ID)

    def test_unsubscribe_subscribed_user(self):
        """Тестируем отписку подписанного пользователя"""
        message = get_mock_tg_message()

        TelegramSubscriber.objects.create(chat_id=CHAT_DEFAULT_ID)

        with patch('tg_subscribers.services.bot.reply_to') as mock_reply_to:
            unsubscribe(message)

            mock_reply_to.assert_called_once_with(message, "❌ Вы отписались от уведомлений")
        assert not TelegramSubscriber.objects.filter(chat_id=12345).exists()

    def test_unsubscribe_non_subscribed_user(self):
        """Тестируем отписку неподписанного пользователя"""
        message = get_mock_tg_message()

        with patch('tg_subscribers.services.bot.reply_to') as mock_reply_to:
            unsubscribe(message)

            mock_reply_to.assert_called_once_with(message, "ℹ️ Вы не были подписаны на уведомления")