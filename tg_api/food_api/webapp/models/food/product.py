from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Boolean, DECIMAL, Numeric
from webapp.models.meta import DEFAULT_SCHEMA
from webapp.models.food.address import Address

from webapp.models.base import BaseDecoder


class Product(BaseDecoder):

    __tablename__ = 'product'
    __table_args__ = ({'schema': DEFAULT_SCHEMA,})

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[DECIMAL] = mapped_column(Numeric)
    quantity: Mapped[int] = mapped_column(Integer)
    image: Mapped[str] = mapped_column(String)
    is_hot: Mapped[bool] = mapped_column(Boolean)
    shop: Mapped[int] = mapped_column(Integer, ForeignKey(f'{DEFAULT_SCHEMA}.shop.id'))

    shops: Mapped[Address] = relationship("Shop")

    _default_fields = [
        "name",
        "quantity",
        "image",
        'is_hot',
        'shop'
    ]

    def to_dict(self) -> dict:
        return dict(self._to_dict(), **{'price': str(self.price)})