from flask import Blueprint

#Blueprint allows us to define views in multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return"<h1>Home</h1>"