from aiogram import executor
from CreateBot import dp
from SingleMode.Handlers import client, CrossAndZero
from InlineMode.Handlers import AnswerInline 
from data_base.data_base import sql_start

if __name__=="__main__":
    client.register_handlers_client(dp)
    CrossAndZero.register_handlers_CrossAndZero(dp)
    AnswerInline.register_handlers_AnswerInline(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=sql_start)
