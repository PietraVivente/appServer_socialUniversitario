from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
from typing_extensions import Annotated

NAMING_CONVENTION = {
    'ix' : 'index_%(column_0_label)s',
    'pk' : 'pk_%(table_name)s',
    'uq' : 'uq_%(table_name)s_%(column_0_name)s',
    'fk' : 'fk_from_%(table_name)s_%(column_0_name)s_to_%(referred_table_name)s)'
}

class Base(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)
    
# data classes
intpk = Annotated[int, mapped_column(primary_key=True)]
name = Annotated[str, mapped_column(String(30))]

db = SQLAlchemy(model_class=Base)

# ToDo db tables
class User(db.Model):
    id : Mapped[intpk] = mapped_column(init=False)
    name : Mapped[name]
    surname : Mapped[name]
    