from aiogram import types, Dispatcher
from CreateBot import bot
from ..Markup import ClientMarkup
import data_base.data_base as data_base


# Может переместить часть с аргументами в другой файл?
async def Greetings(message: types.Message):
    data_base.sign_in(message.from_user.id, message.from_user.first_name)
    await bot.send_message(message.chat.id, r"""
        Добро пожаловать\! Это бот для игры в крестики нолики\. Вы можете выбрать несколько режимов игры\.
        • Со мной \(ботом\) \- \/single\_mode
        • С выбранным другом
        • Со случайным игроком
        """
    )



async def Single_Mode_Settings(message: types.Message):
    await bot.send_message(message.chat.id, "Крестики или нолики?", reply_markup=ClientMarkup.choose_cross_or_zero())    



def register_handlers_client(dp: Dispatcher):
    # Тут message.text=="/start" возможно лишнее!
    dp.register_message_handler(Greetings, lambda message: message.chat.type=='private' and message.get_args()=="", commands=['start'])
    dp.register_message_handler(Single_Mode_Settings, lambda message: message.chat.type=='private', commands=['single_mode'])
