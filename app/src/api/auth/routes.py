from flask import Blueprint
from src.db import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/users/create', methods=['GET'])
def create_user():
    user = User(name = 'Flavio', surname = 'Torresi', matricola='2044116', nickname='tox')
    db.session.add(user)
    db.session.commit()
    
    return 'done'