from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import UserSchema, UserQueryArgsSchema, validate_user_data
from ... import db 
from src.models import SapienzaUser

main_bp = Blueprint('main', 'main', description='rotte principali del sever app')

@main_bp.route('/user/<user_id>')
class UserRoutes(MethodView):
    #@main_bp.arguments(UserQueryArgsSchema, location='query')
    @main_bp.response(200, UserSchema)
    def get(self, user_id):
        
        user = db.get_or_404(SapienzaUser, user_id)
        
        print(user.to_dict())
        
        data = user.to_dict()
        
        res = validate_user_data(data)
        
        if not res['status']:
            print(res['error'])
            abort(422)
        else:
            print('validation successfull...')
        
        
        return data