from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BIND_IP: str
    BIND_PORT: int
    DB_URL: str
    PATH_PREFIX: str = '/api/v1'


settings = Settings()
