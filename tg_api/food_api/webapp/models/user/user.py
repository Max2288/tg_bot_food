from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from webapp.models.base import BaseDecoder
from webapp.models.meta import DEFAULT_SCHEMA, Base


class User(BaseDecoder):

    __tablename__ = "user"
    __table_args__ = {
        "schema": DEFAULT_SCHEMA,
    }

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[String] = mapped_column(String)
