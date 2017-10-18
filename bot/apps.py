from django.apps import AppConfig
import threading
from . import telegram_bot


class BotConfig(AppConfig):
    name = 'bot'
    verbose_name = "Bot application"

    def ready(self):
        # t = threading.Thread(telegram_bot.main())
        # t.run()
         pass
