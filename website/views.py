from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Post
from . import db
import json

#Blueprint allows us to define views in multiple files
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        post = request.form.get('post')

        if len(post) < 1:
            flash('Post is too Short!', category='error')
        else:
            new_post = Post(data=post, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Posted', category='success')

    posts = Post.query.all()

    return render_template("home.html", user=current_user, posts=posts)

@views.route("/contactus")
def contactus():
    return render_template("contactus.html", user=current_user)

@views.route('/delete-post', methods=['POST'])
def delete_post():
    post = json.loads(request.data)
    #loads data as json object
    postId = post['postId']
    post = Post.query.get(postId)
    if post:
        if post.user_id == current_user.id:
            db.session.delete(post)
            db.session.commit()
    #retuns emoty response always needs to retunr
    return jsonify({})