from webapp.models.meta import Base, DEFAULT_SCHEMA

from webapp.models.base import BaseDecoder
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger

class User(BaseDecoder):

    __tablename__ = 'user'
    __table_args__ = ({'schema': DEFAULT_SCHEMA,})

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[String] = mapped_column(String)