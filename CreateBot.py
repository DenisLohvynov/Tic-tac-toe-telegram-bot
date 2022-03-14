from aiogram import Bot, Dispatcher
from decouple import config
import logging

API_TOKEN = config('TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='MarkdownV2')
dp = Dispatcher(bot)
