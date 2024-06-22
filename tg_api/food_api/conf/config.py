from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BIND_IP: str
    BIND_PORT: int
    DB_URL: str
    PATH_PREFIX: str = '/api/v1'
    BUCKET_NAME: str = 'food'
    MINIO_LOGIN: str
    MINIO_PASSWORD:str
    MINIO_URL: str

    API_KEY: str
    JWT_SECRET_SALT: str


settings = Settings()
