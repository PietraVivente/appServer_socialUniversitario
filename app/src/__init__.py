import os
from flask import Flask
from .db import db
from flask_migrate import Migrate
from flask_smorest import Api, Blueprint
from src.config import ProductionConfig, DevelopmentConfig

def create_app(config_class=DevelopmentConfig) -> Flask:
    app = Flask(__name__)
    migrate = Migrate()
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    #api = Api(app)
    
    from .api.main.routes import main_bp
    #api.register_blueprint(main_bp)  ### ToDo quando implementero Flask-Smorest
    app.register_blueprint(main_bp)
    
    from .api.auth.routes import auth_bp
    #api.register_blueprint(auth_bp, url_prefix='/auth')  ### ToDo quando implementero Flask-Smorest
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app