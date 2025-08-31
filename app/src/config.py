### CONTIENE LE CONFIGURAZIONI DEL SERVER ###
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ABCD')
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    API_TITLE = os.getenv('API_TITLE', 'APIdevelop')
    API_VERSION = os.getenv('API_VERSION', 'vDevelop')
    OPENAPI_VERSION = os.getenv('OPENAPI_VERSION', '3.0.2')
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')