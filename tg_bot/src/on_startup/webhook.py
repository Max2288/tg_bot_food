import logging

from aiogram import Bot

from conf.config import settings


async def setup_webhook(bot: Bot) -> None:
    print('Setup webhook')

    webhook = await bot.get_webhook_info()
    if webhook.url != settings.WEBHOOK_URL:
        print('Delete webhook')
        await bot.delete_webhook()

    print('Set webhook')
    await bot.set_webhook(settings.WEBHOOK_URL)

    print('Finish setup')