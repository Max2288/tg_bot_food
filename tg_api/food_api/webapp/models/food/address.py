from sqlalchemy.orm import Mapped, mapped_column
from webapp.models.meta import Base, DEFAULT_SCHEMA
from sqlalchemy import Integer, String, Column
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from shapely import get_coordinates

from webapp.models.base import BaseDecoder


class Address(BaseDecoder):

    __tablename__ = 'address'
    __table_args__ = ({'schema': DEFAULT_SCHEMA,})

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    country: Mapped[String] = mapped_column(String)
    city: Mapped[String] = mapped_column(String)
    street: Mapped[String] = mapped_column(String)
    building_num: Mapped[int] = mapped_column(Integer)
    entrance: Mapped[int] = mapped_column(Integer)
    floor: Mapped[int] = mapped_column(Integer)
    apartment_number: Mapped[int] = mapped_column(Integer)
    coordinates = Column(Geometry('POINT'))

    _default_fields = [
        "country",
        "city",
        "street",
        'building_num',
    ]

    def to_dict(self) -> dict:
        coordinates = get_coordinates(to_shape(self.coordinates)).tolist()
        return dict(self._to_dict(), **{'coordinates':coordinates})
