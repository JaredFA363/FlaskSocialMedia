from flask import Blueprint, render_template, request, flash, redirect,url_for
from website import views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>LogOut</p>"

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(userName) <= 2:
            flash('Username must be greater than 1 characters', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:
            flash('Passwords must be greater than 7 characters', category='error')
        else:
            #add user to db
            new_user = User(email=email, username=userName, password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='successful')
            return redirect(url_for('views.home'))
            

    return render_template("signup.html")

