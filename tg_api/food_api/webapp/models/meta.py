from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

NAMING_CONVENTION = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}


DEFAULT_SCHEMA = 'food'

metadata = MetaData(naming_convention=NAMING_CONVENTION, schema=DEFAULT_SCHEMA)
Base = declarative_base(metadata=metadata)
