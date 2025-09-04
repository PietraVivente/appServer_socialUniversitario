from . import db
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
from typing import Optional
from typing_extensions import Annotated

# data classes : tutti i tipi delle colonne del db
intpk = Annotated[int, mapped_column(primary_key=True)]
name = Annotated[str, mapped_column(String(30))]
second_name = Annotated[Optional[str], mapped_column(String(30), default=None)]
surname = Annotated[str, mapped_column(String(30))]
nickname = Annotated[str, mapped_column(String(30), unique=True)]
matricola = Annotated[int, mapped_column(unique=True)]

# ToDo db tables
class User(db.Model):
    id : Mapped[intpk] = mapped_column(init=False)
    matricola : Mapped[matricola]
    name : Mapped[name]
    #second_name : Mapped[second_name]
    surname : Mapped[surname]
    nickname : Mapped[nickname]
    
    