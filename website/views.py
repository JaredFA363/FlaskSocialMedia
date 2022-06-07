from flask import Blueprint, render_template

#Blueprint allows us to define views in multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")