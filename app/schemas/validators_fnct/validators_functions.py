from marshmallow import ValidationError
from typing import Dict, Any, List
from schemas import user_schema, UserSchema
from src.models import SapienzaUser, Roma3User

# controlla i dati passati per l'user
def validate_user_data(data : SapienzaUser) -> Dict[str, Any]:
    try:
        result = user_schema.load(data)
        return {'status' : 1,
                'returned' : result}
    except ValidationError as error:
        return {'status' : 0,
                'error' : error.messages}
        
# rende gli errori più user-friendly
def format_validationErrors(error : List[str]):
    msgs_tradotti = {}
    
    traduzioni : Dict[str, str] = {
        'email' : 'Indirizzo Email',
        'password' : 'Password',
        'name' : 'Nome',
        'surname' : 'Cognome'
    }
    
    for sezione, messaggio in error:
        trad_chiave = traduzioni.get(sezione, sezione.title())
        msgs_tradotti[trad_chiave] = messaggio
        
    return msgs_tradotti
