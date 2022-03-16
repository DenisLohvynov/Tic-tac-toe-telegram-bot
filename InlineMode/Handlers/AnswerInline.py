from CreateBot import dp, bot, photo_id_inline
from aiogram.types.input_media import InputMediaPhoto
from aiogram.types import InlineQuery, InlineQueryResultCachedPhoto, CallbackQuery
from aiogram import Dispatcher
from InlineMode.Markup import markup

@dp.inline_handler()
async def inline_hander(query: InlineQuery):
    if query.chat_type=='private':
        results = []
        for i in ("X", "O", "?"):
            if query.query in "duel " + i:
                what = "чем\-то?" if i=="?" else i
                results.append(
                    InlineQueryResultCachedPhoto(
                        id=i,
                        photo_file_id=photo_id_inline[i],
                        caption="Хотите сыграть в крестики нолики с игроком " + query.from_user.first_name + f"\. {query.from_user.first_name} играет *{what}*\.",
                        reply_markup= await markup.inline_hander_markup(i, query.from_user.id)
                    )
                )

        await bot.answer_inline_query(query.id, results=results, cache_time=1)


# Вызывать уже после ссылки!
# async def inline_change(callback_query: CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     if callback_query.from_user.id != int(callback_query[1:]):
#         pass
#     # bot.edit_message_caption(

#     # )
#     # with open(GetImage.Generate("NNNNNNNNN"), 'rb') as photo:
#     #     await bot.edit_message_media(
#     #             media=InputMediaPhoto(
#     #                 media=photo,
#     #                 caption="caption"),
#     #             chat_id=callback_query["chat_instance"], 
#     #             message_id=callback_query["inline_message_id"], 
#     #             reply_markup=None
#     #         )


def register_handlers_AnswerInline(dp: Dispatcher):
    dp.register_inline_handler(inline_hander)
    # dp.register_callback_query_handler(inline_change, lambda callback_query: callback_query.data[0] in ('X', 'O', '?'))
