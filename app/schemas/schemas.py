### IL FILE CONTIENE TUTTI GLI SCHEMI DI VALIDAZIONE PRINCIPALI ###
from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class UserSchema(Schema):
    #id = fields.Int(required=True)
    
    matricola = fields.Int(
        required=True,
        validate=validate.Range(min=1000000, max=9999999, error='La matricola deve essere di esattamente 7 caratteri')   
    )
    
    nome = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=30, error='Il nome deve contenere dai 2 ai 30 caratteri')
        )
    
    cognome = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=30, error='Il cognome deve contenere dai 2 ai 30 caratteri')
        )
    
    username = fields.Str(
        validate=validate.Length(min=2, max=20, error='Il nickname deve essere compreso tra 2 e 20 caratteri')
        )
    
    email = fields.Email(error_messages={'main' : 'L\'email inserita non è valida'})
    
    '''personal_hash = fields.Method('gen_hash', dump_only=True)
    
    def gen_hash(self, obj):
        return f'{obj.name}_{obj.surname}_{obj.matricola}'''
    
    
    #email = fields.Email(required = True)
        
    '''password = fields.Str(required=True)
    
    @validates('password')
    def check_password_strenght(self, value, **kwargs):
        if not re.search(r'/d', value):
            raise ValidationError('La password deve contenere almeno un carattere numerico')
        if not re.search(r'[A-Z]', value):
            raise ValidationError('La password deve contenere almeno un carattere maiuscolo') '''
        
user_schema = UserSchema() # mette a disposizione un oggetto per validare lo schema

