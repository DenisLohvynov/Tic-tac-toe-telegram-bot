from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link


async def inline_hander_markup(i: str, user_id: int, inline_message_id: str) -> InlineKeyboardMarkup:
    """
    https://docs.aiogram.dev/en/latest/utils/deep_linking.html
    Добавить время, что бы не работало дольше 5 минут + дату, если изменю, то это еще надо в client.py?
    """
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Принять вызов", url= await get_start_link(i + str(user_id) + " " + inline_message_id, encode=True)))

def temp() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Принять вызов", callback_data="wait"))

def temp_wait() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    # alfabet = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'O'}
    l = [InlineKeyboardButton(i, callback_data="wait") for i in range(9)]
    for i in range(3):
        markup.add(l[3*i], l[3*i+1], l[3*i+2])
    return markup.add(InlineKeyboardButton('Ходи', callback_data="wait"), InlineKeyboardButton('Сдаться', callback_data="wait"))


def your_turn(name: str, id_X: str, message_id_X: str, id_O: str, message_id_O: str, inline_id: str) -> InlineKeyboardMarkup:
    # id - 1, id - 2, message_id-1, message_id-2, name, time?
    alfabet = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'O'}
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(1, callback_data=alfabet[1]+name),
        InlineKeyboardButton(2, callback_data=alfabet[2]+id_X),
        InlineKeyboardButton(3, callback_data=alfabet[3]+id_O)
    )
    markup.add(
        InlineKeyboardButton(4, callback_data=alfabet[4]+message_id_X),
        InlineKeyboardButton(5, callback_data=alfabet[5]+message_id_O),
        InlineKeyboardButton(6, callback_data=alfabet[6]+inline_id)
    )
    markup.add(
        InlineKeyboardButton(7, callback_data=alfabet[7]),
        InlineKeyboardButton(8, callback_data=alfabet[8]),
        InlineKeyboardButton(9, callback_data=alfabet[9])
    )
    return markup.add(InlineKeyboardButton('Ходи', callback_data="wait"), InlineKeyboardButton('Сдаться', callback_data="surrender"))


def not_your_turn(name: str, id_X: str, message_id_X: str, id_O: str, message_id_O: str, inline_id: str) -> InlineKeyboardMarkup:
    # id - 1, id - 2, message_id-1, message_id-2, name, time?
    # alfabet = {1: 'q', 2: 'w', 3: 'e', 4: 'r', 5: 't', 6: 'y', 7: 'u', 8: 'i', 9: 'O'}
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(1, callback_data="expect"+name),
        InlineKeyboardButton(2, callback_data="expect"+id_X),
        InlineKeyboardButton(3, callback_data="expect"+id_O)
    )
    markup.add(
        InlineKeyboardButton(4, callback_data="expect"+message_id_X),
        InlineKeyboardButton(5, callback_data="expect"+message_id_O),
        InlineKeyboardButton(6, callback_data="expect"+inline_id)
    )
    markup.add(
        InlineKeyboardButton(7, callback_data="expect"),
        InlineKeyboardButton(8, callback_data="expect"),
        InlineKeyboardButton(9, callback_data="expect")
    )
    return markup.add(InlineKeyboardButton('Ходи', callback_data="wait"), InlineKeyboardButton('Сдаться', callback_data="surrender"))


async def to_bot():
    return InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти к боту", url= (await get_start_link(""))[:-7]))
