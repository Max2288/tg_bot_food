from sqlalchemy import BigInteger, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from webapp.models.base import BaseDecoder
from webapp.models.food.shop import Shop
from webapp.models.meta import DEFAULT_SCHEMA, Base
from webapp.models.user.user import User


class Feedback(BaseDecoder):

    __tablename__ = "feedback"
    __table_args__ = {
        "schema": DEFAULT_SCHEMA,
    }

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    score: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    user: Mapped[int] = mapped_column(ForeignKey(f"{DEFAULT_SCHEMA}.user.id"))
    shop: Mapped[int] = mapped_column(ForeignKey(f"{DEFAULT_SCHEMA}.shop.id"))

    users: Mapped[User] = relationship()
    shops: Mapped[Shop] = relationship()

    _default_fields = ["score", "description", "user"]