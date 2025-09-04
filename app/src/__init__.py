import os
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from src.config import ProductionConfig, DevelopmentConfig
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass



NAMING_CONVENTION = {
    'ix' : 'index_%(column_0_label)s',
    'pk' : 'pk_%(table_name)s',
    'uq' : 'uq_%(table_name)s_%(column_0_name)s',
    'fk' : 'fk_from_%(table_name)s_%(column_0_name)s_to_%(referred_table_name)s)'
}

class Base(MappedAsDataclass, DeclarativeBase):
    metadata = MetaData(naming_convention=NAMING_CONVENTION)

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app(config_class=DevelopmentConfig) -> Flask:
    
    app = Flask(__name__)
    
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    
    from .api.main.routes import main_bp
    api.register_blueprint(main_bp)  ### ToDo quando implementero Flask-Smorest
    #app.register_blueprint(main_bp)
    
    from .api.auth.routes import auth_bp
    api.register_blueprint(auth_bp)  ### ToDo quando implementero Flask-Smorest
    #app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app