from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ... import db
from src.models import SapienzaUser

auth_bp = Blueprint('auth', 'auth', url_prefix='/auth', description='rotte ausiliarie o secondarie')

@auth_bp.route('/users/', methods=['GET'])
def create_user():
    user = User(name = 'Flavio', surname = 'Torresi', matricola='2044116', nickname='tox')
    db.session.add(user)
    db.session.commit()
    
    return 'done'