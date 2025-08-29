from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    
    from .main.routes import main_bp
    app.register_blueprint(main_bp)
    
    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app