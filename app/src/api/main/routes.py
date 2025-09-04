from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.args_schemas import UserQueryArgsSchema
from schemas.schemas import UserSchema
from src import db
from src.db import User

main_bp = Blueprint('main', 'main', description='rotte principali del sever app')

@main_bp.route('/user/<user_id>')
class UserRoutes(MethodView):
    #@main_bp.arguments(UserQueryArgsSchema, location='query')
    @main_bp.response(200, UserSchema)
    def get(self, user_id):
        
        user = db.get_or_404(User, user_id)
        
        
        return f'<p>Profilo di {user.name}</p>'