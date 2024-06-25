import asyncio

from aiogram.types import BotCommand
from src.integrations.tg_bot import get_dispatcher, get_tg_bot


async def start_polling() -> None:
    bot = get_tg_bot()
    dp = get_dispatcher()
    await bot.delete_webhook()
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start bot"),
        ]
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_polling())
