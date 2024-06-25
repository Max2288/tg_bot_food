from pydantic import BaseModel


class UserRegister(BaseModel):
    id: int
    username: str


class UserLogin(BaseModel):
    id: int
