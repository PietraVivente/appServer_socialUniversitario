### IL FILE CONTIENE TUTTI GLI SCHEMI DI VALIDAZIONE PRINCIPALI ###
from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class UserSchema(Schema):
    name = fields.Str(
        required=True,
        validate=validate.lenght(min=2, max=30, error='Il nome deve contenere dai 2 ai 30 caratteri')
        )
    
    surname = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=30, error='Il cognome deve contenere dai 2 ai 30 caratteri')
        )
    
    email = fields.Email(required = True)
        
    password = fields.Str(required=True)
    
    @validates('password')
    def check_password_strenght(self, value, **kwargs):
        if not re.search(r'/d', value):
            raise ValidationError('La password deve contenere almeno un carattere numerico')
        if not re.search(r'[A-Z]', value):
            raise ValidationError('La password deve contenere almeno un carattere maiuscolo') 
        
user_schema = UserSchema()