from CreateBot import dp, bot, photo_id_inline
from aiogram.utils.deep_linking import decode_payload
from aiogram.types import InlineQuery, InlineQueryResultCachedPhoto, CallbackQuery, Message
from aiogram import Dispatcher
from InlineMode.Markup import markup
from aiogram.types.chosen_inline_result import ChosenInlineResult
from random import choice
import data_base.data_base as data_base
from Utilities import GetImage
# from aiogram.types.input_media import InputMediaPhoto

@dp.inline_handler()
async def inline_hander(query: InlineQuery):
    if query.chat_type=='private':
        results = []
        for i in ("X", "O", "?"):
            if query.query in "duel " + i:
                results.append(
                    InlineQueryResultCachedPhoto(
                        id=i,
                        photo_file_id=photo_id_inline[i],
                        caption="Подождите\.",
                        reply_markup=markup.temp()
                    )
                )

        await bot.answer_inline_query(query.id, results=results, cache_time=1)


@dp.chosen_inline_handler()
async def chosen_handler(chosen_result: ChosenInlineResult):
    what = "чем\-то" if chosen_result.result_id=="?" else chosen_result.result_id
    await bot.edit_message_caption(
        inline_message_id=chosen_result.inline_message_id,
        caption="Хотите сыграть в крестики нолики с игроком " + chosen_result.from_user.first_name + "\. " + chosen_result.from_user.first_name + " играет *" + what + "*\.",
        reply_markup= await markup.inline_hander_markup(chosen_result.result_id, chosen_result.from_user.id, chosen_result.inline_message_id)
        )


# тут обращения в БД за именами
async def Greetings(message: Message):
    data_base.sign_in(message.from_user.id, message.from_user.first_name)
    args = message.get_args()
    payload = decode_payload(args)
    if message.from_user.id==int(payload[1:].split(' ')[0]):
        await bot.send_message(message.chat.id, r"""
            Если Вы хотите сыграть с собой, есть способ по проще :\-\)\.
            """
        )
    else:
        X_O = payload[0] if payload[0]!='?' else choice(('X', 'O'))
        id_X_O, inline_id = payload[1:].split(' ') # id first, plays X_O
        id_O_X = str(message.from_user.id) # id second
        try:
            await bot.edit_message_caption(
                inline_message_id=inline_id,
                caption=data_base.get_name(int(id_X_O)) + " и " + message.from_user.first_name + " сейчас играют\."
            )
            with open(GetImage.Generate("NNNNNNNNN"), 'rb') as photo:
                file_id = (await bot.send_photo(
                    id_X_O,
                    photo,
                    caption='Выберите Ваш ход из предложенных ниже:',
                    reply_markup=None
                ))["photo"][2]["file_id"]
                await bot.send_photo(
                    id_O_X,
                    file_id,
                    caption='Выберите Ваш ход из предложенных ниже:',
                    reply_markup=None
                )

        except NameError:
            await bot.edit_message_caption(
                inline_message_id=inline_id,
                caption="Кто\-то не нажал [старт]("+r"https://t.me/" + (await bot.get_me()).username + "?start" + ")\. *Нажмите* и затем бросьте еще одно предложения об игре\."
            )

async def wait(callback_query: CallbackQuery):
    await callback_query.answer("Подождите бот генерирует кнопку.", show_alert=False)
    await bot.answer_callback_query(callback_query.id)


def register_handlers_AnswerInline(dp: Dispatcher):
    dp.register_inline_handler(inline_hander)
    dp.register_message_handler(Greetings, lambda message: message.get_args()!='', commands=['start'])
    dp.register_chosen_inline_handler(chosen_handler)
    dp.register_callback_query_handler(wait, lambda callback_query: callback_query.data=="wait")
