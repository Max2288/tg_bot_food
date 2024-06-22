from webapp.models.meta import Base, DEFAULT_SCHEMA

from webapp.models.base import BaseDecoder
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BigInteger, Integer, ForeignKey

from webapp.models.user.user import User

from webapp.models.food.shop import Shop


class Feedback(Base):

    __tablename__ = 'feedback'
    __table_args__ = ({'schema': DEFAULT_SCHEMA,})

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    score: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String)
    user: Mapped[int] = mapped_column(ForeignKey(f'{DEFAULT_SCHEMA}.user.id'))
    shop: Mapped[int] = mapped_column(ForeignKey(f'{DEFAULT_SCHEMA}.shop.id'))

    users: Mapped[User] = relationship()
    shops: Mapped[Shop] = relationship()
