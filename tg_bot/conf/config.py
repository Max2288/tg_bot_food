from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FOOD_BACKEND_HOST: str = "http://web:1025"

    BOT_TOKEN: str
    WEBHOOK_URL: str = ""

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str
    REDIS_DB: int = 0

    LOG_LEVEL: str = ""

    RETRY_COUNT: int = 3

    MAX_DELIVERY_WAIT_TIME: int = 60 * 10

    BUCKET_NAME: str = "food"
    MINIO_LOGIN: str
    MINIO_PASSWORD: str
    MINIO_URL: str

    API_KEY: str


settings = Settings()
