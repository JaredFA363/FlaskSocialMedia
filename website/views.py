from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db
import json

#Blueprint allows us to define views in multiple files
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('views.create_post'))

    posts = Post.query.all()

    return render_template("home.html", user=current_user, posts=posts[::-1])

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

@views.route('/create-post', methods=['GET','POST'])
@login_required
def create_post():
    if request.method == 'POST':
        post = request.form.get('post')
        link = request.form.get('link')
        
        if len(post) < 1 or len(link) < 1:
            flash('Post is too Short!', category='error')
        else:
            new_post = Post(data=post,link = link, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Posted: return to home', category='success')
            
    return render_template("createpost.html",user=current_user)