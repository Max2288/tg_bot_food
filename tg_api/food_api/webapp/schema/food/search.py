from pydantic import BaseModel


class ShopResponse(BaseModel):
    id: int
    name: str
    description: str
    image: str
    address: int
