from marshmallow import ValidationError
from typing import Dict, Any, List
from schemas.schemas import user_schema

# controlla i dati passati per l'user
def validate_user_data(data : Dict[str, Any]) -> Dict[str, Any]:
    try:
        result = user_schema.load(data)
        return {'status' : 'success',
                'returned' : result}
    except ValidationError as error:
        return {'status' : 'error',
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

