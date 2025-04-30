# conftest.py
import pytest
from django.contrib.auth.models import User
from django.test import RequestFactory
from tg_subscribers.models import TelegramSubscriber
from tg_subscribers.tests.mocks import CHAT_DEFAULT_ID


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='12345')


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def admin_request(request_factory):
    request = request_factory.get('/admin/')
    return request


@pytest.fixture
def telegram_subscriber():
    return TelegramSubscriber.objects.create(chat_id=CHAT_DEFAULT_ID)