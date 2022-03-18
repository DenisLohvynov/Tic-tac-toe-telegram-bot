from CreateBot import dp, bot, photo_id_inline
from aiogram.types import InlineQuery, InlineQueryResultCachedPhoto, CallbackQuery
from aiogram import Dispatcher
from InlineMode.Markup import markup
from aiogram.types.chosen_inline_result import ChosenInlineResult


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


async def chosen_handler(chosen_result: ChosenInlineResult):
    what = "чем\-то" if chosen_result.result_id=="?" else chosen_result.result_id
    await bot.edit_message_caption(
        inline_message_id=chosen_result.inline_message_id,
        caption="Хотите сыграть в крестики нолики с игроком " + chosen_result.from_user.first_name + "\. " + chosen_result.from_user.first_name + " играет *" + what + "*\.",
        reply_markup= await markup.inline_hander_markup(chosen_result.result_id, chosen_result.from_user.id, chosen_result.inline_message_id)
        )



async def wait(callback_query: CallbackQuery):
    await callback_query.answer("Подождите бот генерирует кнопку.", show_alert=False)
    await bot.answer_callback_query(callback_query.id)


def register_handlers_AnswerInline(dp: Dispatcher):
    dp.register_inline_handler(inline_hander)
    dp.register_chosen_inline_handler(chosen_handler)
    dp.register_callback_query_handler(wait, lambda callback_query: callback_query.data[:4]=="wait")
