import asyncio
from asyncio import Task
from typing import Any

from aiogram import Bot, Dispatcher, types
from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from src.integrations.tg_bot import get_dispatcher, get_tg_bot
from src.utils.background_tasks import tg_background_tasks
from starlette.requests import Request

router = APIRouter()


@router.post("/tg")
async def tg_api(
    request: Request,
    dp: Dispatcher = Depends(get_dispatcher),
    bot: Bot = Depends(get_tg_bot),
) -> ORJSONResponse:
    data = await request.json()
    update = types.Update(**data)

    task: Task[Any] = asyncio.create_task(dp.feed_webhook_update(bot, update))
    tg_background_tasks.add(task)

    task.add_done_callback(tg_background_tasks.discard)

    print(data)

    return ORJSONResponse({"success": True})
