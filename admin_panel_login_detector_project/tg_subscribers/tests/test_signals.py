from unittest.mock import patch

import pytest
from django.contrib.auth.models import User

from tg_subscribers.signals import send_login_notification


@pytest.mark.django_db
class TestSignals:
    def test_send_login_notification_for_admin(self, admin_request, user, telegram_subscriber):
        """Тестируем отправку уведомления при входе в админку"""
        with patch('tg_subscribers.services.bot.send_message') as mock_send:
            send_login_notification(sender=User, request=admin_request, user=user)

            mock_send.assert_called_once()
            args, kwargs = mock_send.call_args
            assert kwargs['chat_id'] == telegram_subscriber.chat_id
            assert user.username in kwargs['text']
