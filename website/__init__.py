from flask import Flask

#initialising app

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'my secret'

    return app