from . import db
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
from typing import Optional, Literal
from typing_extensions import Annotated
from werkzeug.security import generate_password_hash, check_password_hash

# data classes : tutti i tipi delle colonne del db
intpk = Annotated[int, mapped_column(primary_key=True)]
name = Annotated[str, mapped_column(String(30))]
second_name = Annotated[Optional[str], mapped_column(String(30), default=None)]
surname = Annotated[str, mapped_column(String(30))]
username = Annotated[str, mapped_column(String(30), unique=True)]
matricola = Annotated[int, mapped_column(unique=True)]

# ToDo db tables
class SapienzaUser(db.Model):
    id : Mapped[intpk] = mapped_column(init=False)
    matricola : Mapped[matricola]
    name : Mapped[name]
    second_name : Mapped[second_name]
    surname : Mapped[surname]
    username : Mapped[username]
    email : Mapped[str] = mapped_column(String(50), unique=True)
    password : Mapped[str] = mapped_column(String(256), default=None, nullable=False)
    
    def set_password(self, sub_psw: str) -> None:
        self.password = generate_password_hash(sub_psw)
        
    def check_password(self, sub_psw: str) -> bool:
        return check_password_hash(self.password, sub_psw)
    
    def to_dict(self):
        return {
            'matricola' : self.matricola,
            'nome' : self.name,
            'cognome' : self.surname,
            'username' : self.username,
            'email' : self.email
        }
        
class Roma3User(db.Model):
    id : Mapped[intpk] = mapped_column(init=False)
    matricola : Mapped[matricola]
    name : Mapped[name]
    second_name : Mapped[second_name]
    surname : Mapped[surname]
    username : Mapped[username]
    email : Mapped[str] = mapped_column(String(50), unique=True)
    password : Mapped[str] = mapped_column(String(256), default=None, nullable=False)
    
    def set_password(self, sub_psw: str) -> None:
        self.password = generate_password_hash(sub_psw)
        
    def check_password(self, sub_psw: str) -> bool:
        return check_password_hash(self.password, sub_psw)
    
    def to_dict(self):
        return {
            'matricola' : self.matricola,
            'nome' : self.name,
            'cognome' : self.surname,
            'username' : self.username,
            'email' : self.email
        }