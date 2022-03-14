from aiogram import executor
from CreateBot import dp
from SingleMode.Handlers import client, CrossAndZero


if __name__=="__main__":
    client.register_handlers_client(dp)
    CrossAndZero.register_handlers_CrossAndZero(dp)
    executor.start_polling(dp, skip_updates=True)

# Добавить цвет крестикам (синий) и ноликам (зеленый)?
# Изменить ожидания при игре с ботом?