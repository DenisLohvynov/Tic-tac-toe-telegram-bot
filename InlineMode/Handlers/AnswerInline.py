from CreateBot import dp, bot, photo_id_inline
# import hashlib
from aiogram.types import InlineQuery, InlineQueryResultCachedPhoto
from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.inline_handler()
async def inline_hander(query: InlineQuery):
    if query.chat_type=='private':
        results = []
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Принять вызов", callback_data="1"))
        for i in ("X", "O", "?"):
            if query.query in "duel " + i:
                what = "чем\-то?" if i=="?" else i
                results.append(
                    InlineQueryResultCachedPhoto(
                        id=i,
                        photo_file_id=photo_id_inline[i],
                        caption="Хотите сыграть в крестики нолики с игроком " + query.from_user.first_name + f"\. {query.from_user.first_name} играет *{what}*\.",
                        reply_markup=markup
                    )
                )

        await bot.answer_inline_query(query.id, results=results, cache_time=1)


def register_handlers_AnswerInline(dp: Dispatcher):
    dp.register_inline_handler(inline_hander)
