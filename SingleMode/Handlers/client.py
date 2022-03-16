from aiogram import types, Dispatcher
from CreateBot import bot
from ..Markup import ClientMarkup
from aiogram.utils.deep_linking import decode_payload


# Может переместить часть с аргументами в другой файл?
async def Greetings(message: types.Message):
    args = message.get_args()
    if args=="":
        await bot.send_message(message.chat.id, r"""
            Добро пожаловать\! Это бот для игры в крестики нолики\. Вы можете выбрать несколько режимов игры\.
            • Со мной \(ботом\) \- \/single\_mode
            • С выбранным другом
            • Со случайным игроком
            """
        )
    else:    
        payload = decode_payload(args)
        print(payload)
        if message.from_user.id==int(payload[1:]):
            await bot.send_message(message.chat.id, r"""
                Если Вы хотите сыграть с собой, есть способ по проще :\-\)\.
                """
            )
        else:
            pass



async def Single_Mode_Settings(message: types.Message):
    await bot.send_message(message.chat.id, "Крестики или нолики?", reply_markup=ClientMarkup.choose_cross_or_zero())    



def register_handlers_client(dp: Dispatcher):
    # Тут message.text=="/start" возможно лишнее!
    dp.register_message_handler(Greetings, lambda message: message.chat.type=='private', commands=['start'])
    dp.register_message_handler(Single_Mode_Settings, lambda message: message.chat.type=='private', commands=['single_mode'])
