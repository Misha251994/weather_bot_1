from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

#make menu in bot
async def commands(bot:Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start work'
        ),
        BotCommand(
            command='cancel',
            description='cancellation of the command'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())