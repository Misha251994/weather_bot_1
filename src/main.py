import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

from src.handlers import weather_handlers
from src.utils.command import commands


load_dotenv()



async def start_bot(bot: Bot):
    await commands(bot)
    await bot.send_message(585210091, text='Bot start')

async def stop_bot(bot: Bot):
    await bot.send_message(585210091, text='Bot stop ')

async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    dp = Dispatcher()
    bot = Bot(os.getenv("BOT_TOKEN"))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(weather_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print('Bot not work')
