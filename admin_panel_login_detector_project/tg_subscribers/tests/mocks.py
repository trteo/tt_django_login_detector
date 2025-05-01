from unittest.mock import patch, MagicMock
from telebot import types

CHAT_DEFAULT_ID = 12345
MESSAGE_DEFAULT_ID = 1111


def get_mock_tg_chat(chat_id: int = CHAT_DEFAULT_ID) -> types.Chat:
    chat = MagicMock(spec=types.Chat)
    chat.id = chat_id
    return chat


def get_mock_tg_message(message_id: int = MESSAGE_DEFAULT_ID, chat: types.Chat = None) -> types.Message:
    if chat is None:
        chat = get_mock_tg_chat()

    message = MagicMock(spec=types.Message)
    message.chat = chat
    message.message_id = message_id
    return message


