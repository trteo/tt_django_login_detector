import os
import sys
import threading

from django.apps import AppConfig


class TgSubscribersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tg_subscribers'

    def ready(self):
        # Импорт сигналов при старте приложения
        import tg_subscribers.signals
        import tg_subscribers.bot_handlers

        # Запускаем бота только в основном процессе, не при релоаде
        if os.environ.get('RUN_MAIN') == 'true':
            self.start_bot()

    def start_bot(self):
        if not hasattr(self, '_bot_thread'):
            self._bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            self._bot_thread.start()

    @staticmethod
    def run_bot():
        print("Starting Telegram bot...")
        try:
            from tg_subscribers.services import bot
            bot.infinity_polling()
        except Exception as e:
            print(f"Bot error: {e}")