### IL FILE CONTIENE I VALIDATORI DEGLI ARGOMENTI DELLE CHIAMATE ALLE API ###
from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class UserQueryArgsSchema(Schema):
    email = fields.Str(required=True) 
    