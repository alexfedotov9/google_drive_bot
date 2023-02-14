from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_instruction(message: types.Message):
    await message.reply('Привет! Это инструкция по работе с ботом.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)