from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from .config import Config
# from dotenv import load_dotenv

# load_dotenv()


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    from .main.routes import main
    app.register_blueprint(main)

    from .movies.routes import movies
    app.register_blueprint(movies)

    from .shows.routes import tv
    app.register_blueprint(tv)
    from .users.routes import user
    app.register_blueprint(user)
    
    return app

