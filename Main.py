from aiogram import executor
from CreateBot import dp
from SingleMode.Handlers import client, CrossAndZero as CrossAndZero1
from InlineMode.Handlers import AnswerInline, CrossAndZero as CrossAndZero2
from data_base.data_base import sql_start


if __name__=="__main__":
    client.register_handlers_client(dp)
    CrossAndZero1.register_handlers_CrossAndZero(dp)
    AnswerInline.register_handlers_AnswerInline(dp)
    CrossAndZero2.register_handlers_CrossAndZero(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=sql_start)
