import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Initialize bot with token
TOKEN = "8027658252:AAH53Ut2uIkZsTyztyivDssIls4-mQ3hZC0"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Command handler for /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello! I am your Telegram bot 🤖")

# Echo handler (repeats user messages)
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"You said: {message.text}")

# Start the bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
