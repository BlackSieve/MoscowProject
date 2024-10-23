import asyncio
from aiogram import Bot, Dispatcher

from app.database import db_start
from keyboard.handlers import router
from game.quize_game import game
from dotenv import load_dotenv
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


async def startup(_):
    await db_start()
    print('Бот запущен!')


async def main():
    dp.include_routers(router,game)
    await dp.start_polling(bot, on_startup=startup)


if __name__ == '__main__':
    asyncio.run(main())
