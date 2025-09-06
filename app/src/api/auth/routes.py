from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ... import db
from src.models import SapienzaUser

auth_bp = Blueprint('auth', 'auth', url_prefix='/auth', description='rotte ausiliarie o secondarie')

# metodo di prova per popolare il db
@auth_bp.route('/users/', methods=['GET'])
def create_user():
    user = SapienzaUser(name = 'Flavio', surname = 'Torresi', matricola='2044116', username='tox', email='flavio@prova.torresi', second_name=None, password=None)
    user.set_password('password') # usa il metodo della classe per settare la password con salting e hashing
    
    db.session.add(user)
    db.session.commit()
    
    return 'done'

#TODO checks if the psw hash is correct calling SapienzaUser.check_password() on the new user