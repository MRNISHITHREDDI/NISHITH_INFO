from telethon import TelegramClient
from decouple import config
from os import getenv
import logging
import time
import os

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

Raizen = TelegramClient('Raizen', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
