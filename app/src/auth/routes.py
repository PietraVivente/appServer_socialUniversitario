from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/prova')
def prova():
    return 'prova effettuata'