from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
bot=Bot(token="6835043572:AAFBEoLuRf-m36ByyubJlhAjFroNGWvkBXc")
dispatcher= Dispatcher(bot)


@dispatcher.message_handler()
async def handle_message(message: types.Message):
    await message.answer(message.text)
executor.start_polling(dispatcher, skip_updates=True)

