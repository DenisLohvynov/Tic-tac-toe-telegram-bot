import re
from InlineMode.Markup import markup
from data_base import data_base
from aiogram.types import Message, CallbackQuery
from CreateBot import bot, dp
from Utilities import CodeForCallbackMove as code, GetImage, FunctionsForTicTacToe
from aiogram import Dispatcher
from aiogram.types.input_media import InputMediaPhoto


async def deep_link(message: Message):
    data_base.sign_in(message.from_user.id, message.from_user.first_name)
    id_X, id_O, inline_id = code.decode_greetings_2_0(message.get_args(), str(message.from_user.id))
    if id_X==id_O:
        await bot.send_message(message.chat.id, r"""
            Если Вы хотите сыграть с собой, есть способ по проще :\-\)\.
            """
        )
    else:
        try:
            await bot.edit_message_caption(
                inline_message_id=inline_id,
                caption=data_base.get_name(int(id_X)) + " и " + data_base.get_name(int(id_O)) + " сейчас играют\.",
                reply_markup=await markup.to_bot()
            )
            with open(GetImage.Generate("NNNNNNNNN"), 'rb') as photo:
                data1 = (await bot.send_photo(
                    id_X,
                    photo,
                    caption='Выберите Ваш ход из предложенных ниже:',
                    reply_markup=markup.temp_wait()
                ))
                file_id = data1["photo"][2]["file_id"]
                data2= await bot.send_photo(
                    id_O,
                    file_id,
                    caption='Подождите соперник ходит\.',
                    reply_markup=markup.temp_wait()
                )
                await bot.edit_message_reply_markup(
                        chat_id=id_X, 
                        message_id=data1["message_id"],
                        reply_markup=markup.your_turn("NNNNNNNNN", id_X, str(data1["message_id"]), id_O, str(data2["message_id"]))
                    )
                await bot.edit_message_reply_markup(
                        chat_id=id_O, 
                        message_id=data2["message_id"],
                        reply_markup=markup.not_your_turn("NNNNNNNNN", id_X, str(data1["message_id"]), id_O, str(data2["message_id"]))
                    )
        except NameError:
            await bot.edit_message_caption(
                inline_message_id=inline_id,
                caption="Кто\-то не нажал [старт]("+r"https://t.me/" + (await bot.get_me()).username + "?start" + ")\. *Нажмите* и затем бросьте еще одно предложения об игре\."
            )


async def expect(callback_query: CallbackQuery):
    await callback_query.answer("Ход соперника.", show_alert=False)
    await bot.answer_callback_query(callback_query.id)


async def move(callback_query: CallbackQuery):
    alfabet = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6,'u': 7,'i': 8, 'O': 9}
    D = code.decode_data_from_markup_your_turn(callback_query["message"]["reply_markup"]["inline_keyboard"])
    if D["name"][alfabet[callback_query.data[0]]-1]!='N':
        await callback_query.answer("Ход не может быть совершен.", show_alert=True)
        await bot.answer_callback_query(callback_query.id)
    else:
        await callback_query.answer("Ход совершен.", show_alert=False)
        await bot.answer_callback_query(callback_query.id)
        if str(callback_query.message.chat.id)==D["id_X"]:
            name = FunctionsForTicTacToe.get_new_name(D["name"], alfabet[callback_query.data[0]]-1, X='X')
            chat_id1 = int(D["id_O"])
            message_id1 = int(D["message_id_O"])
            # print("X")
        else:
            name = FunctionsForTicTacToe.get_new_name(D["name"], alfabet[callback_query.data[0]]-1, X='O')
            chat_id1 = int(D["id_X"])
            message_id1 = int(D["message_id_X"])
            # print("O")

        with open(GetImage.Generate(name), 'rb') as photo:
            file_id = (await bot.edit_message_media(
                    media=InputMediaPhoto(
                        media=photo,
                        caption='Подождите соперник ходит\.'),
                    chat_id=callback_query.message.chat.id, 
                    message_id=callback_query.message.message_id, 
                    reply_markup=markup.not_your_turn(name, D["id_X"], D["message_id_X"], D["id_O"], D["message_id_O"])
                ))["photo"][2]["file_id"]
            await bot.edit_message_media(
                    media=InputMediaPhoto(
                        media=file_id,
                        caption='Выберите Ваш ход из предложенных ниже:'),
                    chat_id=chat_id1, 
                    message_id=message_id1,
                    reply_markup=markup.your_turn(name, D["id_X"], D["message_id_X"], D["id_O"], D["message_id_O"])
                )


def register_handlers_CrossAndZero(dp: Dispatcher):
    dp.register_message_handler(deep_link, lambda message: message.get_args()!='', commands=['start'])
    dp.register_callback_query_handler(expect, lambda callback_query: callback_query.data[:6]=="expect")
    dp.register_callback_query_handler(move, lambda callback_query: callback_query.data[0] in ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'O'))
