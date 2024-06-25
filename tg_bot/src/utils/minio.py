import aiohttp
from aiogram.types import BufferedInputFile
from conf.config import settings
from miniopy_async import Minio

minio_client = Minio(
    settings.MINIO_URL,
    access_key=settings.MINIO_LOGIN,
    secret_key=settings.MINIO_PASSWORD,
    secure=False,
)


async def get_file_from_minio(object_name):
    async with aiohttp.ClientSession() as session:
        response = await minio_client.get_object(
            settings.BUCKET_NAME, object_name, session=session
        )
        file_data = await response.read()
        return file_data


async def get_input_file(filename: str):
    image_file = await get_file_from_minio(filename)
    input_file = BufferedInputFile(image_file, filename=filename.split("/")[1])
    return input_file
