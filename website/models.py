from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    link = db.Column(db.String(1000))
    #date = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.DateTime, default=datetime.now())
    userpost = db.relationship('User', backref='post', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    posts = db.relationship('Post')