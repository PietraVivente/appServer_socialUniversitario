import os
from flask import Flask
from .db import db
from flask_migrate import Migrate
from flask_smorest import Api, Blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config.from_object('src.config.DevelopmentConfig')
    
    db.init_app(app)
    Migrate(app, db)
    #api = Api(app)
    
    with app.app_context():
        db.create_all()
    
    from .api.main.routes import main_bp
    #api.register_blueprint(main_bp)  ### ToDo quando implementero Flask-Smorest
    app.register_blueprint(main_bp)
    
    from .api.auth.routes import auth_bp
    #api.register_blueprint(auth_bp, url_prefix='/auth')  ### ToDo quando implementero Flask-Smorest
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app