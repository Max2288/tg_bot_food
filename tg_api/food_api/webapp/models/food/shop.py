from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from webapp.models.meta import DEFAULT_SCHEMA
from webapp.models.food.address import Address

from webapp.models.base import BaseDecoder

from webapp.models.food.product import Product


class Shop(BaseDecoder):

    __tablename__ = 'shop'
    __table_args__ = ({'schema': DEFAULT_SCHEMA,})

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String)
    address: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DEFAULT_SCHEMA}.address.id'))

    addresses: Mapped[Address] = relationship("Address")

    _default_fields = [
        "name",
        "description",
        "image",
        'address'
    ]
