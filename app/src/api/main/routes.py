from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.args_schemas import UserQueryArgsSchema
from schemas.schemas import UserSchema
from schemas.validators_fnct import validators_functions as vf
from src import db
from src.db import User as UserModel

main_bp = Blueprint('main', 'main', description='rotte principali del sever app')

@main_bp.route('/user/<user_id>')
class UserRoutes(MethodView):
    #@main_bp.arguments(UserQueryArgsSchema, location='query')
    @main_bp.response(200, UserSchema)
    def get(self, user_id):
        
        user = db.get_or_404(UserModel, user_id)
        
        print(user)
        
        res = vf.validate_user_data(user)
        
        if not res['status']:
            print(res.error)
            abort(422)
        
        
        return f'{user}'