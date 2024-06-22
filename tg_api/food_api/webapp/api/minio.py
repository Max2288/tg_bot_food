from fastapi import APIRouter, HTTPException, status, UploadFile, File
from fastapi.responses import ORJSONResponse
from loguru import logger

from miniopy_async import Minio

from conf.config import settings

router = APIRouter()

client = Minio(
    settings.MINIO_URL,
    access_key=settings.MINIO_LOGIN,
    secret_key=settings.MINIO_PASSWORD,
    secure=False
)

async def create_bucket_if_not_exists(bucket_name):
    exists = await client.bucket_exists(bucket_name)
    if not exists:
        await client.make_bucket(bucket_name)
        logger.info(f"Bucket '{bucket_name}' created.")
    else:
        logger.info(f"Bucket '{bucket_name}' already exists.")


@router.post("/load", status_code=status.HTTP_200_OK)
async def load_to_minio(save_name: str, file: UploadFile = File(...)):
    await create_bucket_if_not_exists(settings.BUCKET_NAME)
    try:
        file_length = len(await file.read())
        await file.seek(0)
        file_path = f"files/{save_name}.jpg"

        # Проверка содержимого файла
        logger.debug(f"Uploading file to {file_path}, size: {file_length} bytes")

        await client.put_object(
            bucket_name=settings.BUCKET_NAME,
            object_name=file_path,
            data=file,
            length=file_length
        )
        logger.info(f"File {file_path} successfully uploaded to bucket {settings.BUCKET_NAME}.")
        return ORJSONResponse({"message": "success"})
    except Exception as e:
        logger.error(f"Произошла ошибка во время загрузки файла: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
