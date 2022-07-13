from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB = "database.db"

#initialising app

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'my secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Post

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('website/' + DB ):
        db.create_all(app=app)
        print('Created Database!')