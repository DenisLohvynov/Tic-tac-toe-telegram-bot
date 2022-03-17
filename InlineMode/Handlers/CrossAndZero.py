from InlineMode.Markup import markup
from data_base import data_base
from aiogram.types import Message
from random import choice
from CreateBot import bot, dp
from Utilities import CodeForCallbackMove as code, GetImage
from aiogram import Dispatcher


async def Greetings(message: Message):
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
                caption=data_base.get_name(int(id_X)) + " и " + data_base.get_name(int(id_O)) + " сейчас играют\."
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


def register_handlers_CrossAndZero(dp: Dispatcher):
    dp.register_message_handler(Greetings, lambda message: message.get_args()!='', commands=['start'])
