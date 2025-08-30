### CONTIENE LE CONFIGURAZIONI DEL SERVER ###
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ABCD')
    DEBUG = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DB_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DB_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')