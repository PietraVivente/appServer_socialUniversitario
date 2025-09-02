from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.args_schemas import UserQueryArgsSchema
from schemas.schemas import UserSchema
from src.db import db

main_bp = Blueprint('main', 'main', description='rotte principali del sever app')

@main_bp.route('/')
class User(MethodView):
    @main_bp.arguments(UserQueryArgsSchema, location='query')
    @main_bp.response(200, UserSchema(many=True))
    def get(self, args):
        db.session.execute() # TODO