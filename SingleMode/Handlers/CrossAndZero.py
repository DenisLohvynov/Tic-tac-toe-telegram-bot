from aiogram import types, Dispatcher, Bot
from aiogram.types.input_media import InputMediaPhoto
import asyncio
from CreateBot import bot, dp
from Utilities import FunctionsForTicTacToe, GetImage
from ..Markup import ClientMarkup
from Utilities import CodeForCallbackMove

async def Opponent_Turn(callback_query: types.CallbackQuery):
    await callback_query.answer("Ход оппонента", show_alert=True)
    await bot.answer_callback_query(callback_query.id)


async def process_callback_X_O(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    name = "NNNNNNNNN" if callback_query.data=="Cross" else FunctionsForTicTacToe.get_random("NNNNNNNNN", what='X')
    with open(GetImage.Generate(name), 'rb') as photo:
        await bot.send_photo(
                callback_query.message.chat.id,
                photo,
                caption='Выберите Ваш ход из предложенных ниже:',
                reply_markup=ClientMarkup.choose_move(name)
            )


@dp.callback_query_handler(lambda callback_query: (callback_query.data[0] in [str(i) for i in range(1, 10)]) and callback_query.message.chat.type=='private')
async def process_callback_i(callback_query: types.CallbackQuery):
    
    async def answer(bot: Bot,  callback_query: types.CallbackQuery, name: str, answer: str, caption: str, show_alert: bool = True, markup: types.InlineKeyboardMarkup = None):
        await callback_query.answer(answer, show_alert=show_alert)
        await bot.answer_callback_query(callback_query.id)
        
        with open(GetImage.Generate(name), 'rb') as photo:
            await bot.edit_message_media(
                    media=InputMediaPhoto(
                        media=photo,
                        caption=caption),
                    chat_id=callback_query.message.chat.id, 
                    message_id=callback_query.message.message_id, 
                    reply_markup=markup
                )

    t = int(callback_query.data[0])-1 # index
    name_old = CodeForCallbackMove.decode(callback_query.data[1:])
    if name_old[t]!='N':
        await callback_query.answer("Ход не может быть совершен.", show_alert=True)
        await bot.answer_callback_query(callback_query.id)
    else:
        name = FunctionsForTicTacToe.get_new_name(name_old, t)
        temp = FunctionsForTicTacToe.if_end(name)
        if temp==1:
            await answer(bot, callback_query, name, "Победа!", "Победа\!")
        elif temp==2:
            await answer(bot, callback_query, name, "Ничья.", "Ничья\.")
        else:
            name = FunctionsForTicTacToe.get_random(name)
            temp = FunctionsForTicTacToe.if_end(name)
            if temp==1:
                await answer(bot, callback_query, name, "Поражение.", "Вы проиграли\!")
            elif temp==2:
                await answer(bot, callback_query, name, "Ничья.", "Ничья\.")
            else:
                await answer(bot, callback_query, name, "Ход совершен.", "Выберите Ваш ход из предложенных ниже:", show_alert=False, markup=ClientMarkup.choose_move(name))


def register_handlers_CrossAndZero(dp: Dispatcher):
    dp.register_callback_query_handler(Opponent_Turn, lambda callback_query: (callback_query.data == "OpponentTurn") and callback_query.message.chat.type=='private')
    dp.register_callback_query_handler(process_callback_X_O, lambda callback_query: callback_query.data in ("Zero", "Cross"))
