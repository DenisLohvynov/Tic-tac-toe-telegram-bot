from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link


async def inline_hander_markup(i: str, user_id: int, inline_message_id: str) -> InlineKeyboardMarkup:
    """
    https://docs.aiogram.dev/en/latest/utils/deep_linking.html
    Добавить время, что бы не работало дольше 5 минут + дату, если изменю, то это еще надо в client.py?
    """
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Принять вызов", url= await get_start_link(i + str(user_id) + " " + inline_message_id, encode=True)))

def temp():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Принять вызов", callback_data="wait"))
