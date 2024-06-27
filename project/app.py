from init import create_app, db
from flask import render_template, redirect, url_for, request, session, send_from_directory
from forms import RegistrationForm, LoginForm, LightUploadForm
from models import User, Light
from utils import validate_username, validate_email, validate_password
import os

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if not validate_username(form.username.data):
            form.username.errors.append("Username already taken.")
        if not validate_email(form.email.data):
            form.email.errors.append("Invalid email format.")
        if not validate_password(form.password.data):
            form.password.errors.append("Password does not meet security requirements.")
        if form.errors:
            return render_template('register.html', form=form)
        
        user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        session['username'] = user.username
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['username'] = user.username
            return redirect(url_for('home'))
        form.password.errors.append('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/account')
def account():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = User.query.filter_by(username=session['username']).first()
    return render_template('account.html', user=user)

@app.route('/swiper_home')
def swiper_home():
    return render_template('swiper_home.html')

@app.route('/builder_home')
def builder_home():
    return render_template('builder_home.html')

@app.route('/swiper_categories')
def swiper_categories():
    return render_template('swiper_categories.html')

@app.route('/swiper_lights')
def swiper_lights():
    return render_template('swiper_lights.html')

@app.route('/builder_upload', methods=['GET', 'POST'])
def builder_upload():
    form = LightUploadForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=session['username']).first()
        light = Light(
            name=form.name.data,
            category=form.category.data,
            price=form.price.data,
            color=form.color.data,
            height=form.height.data,
            builder_id=user.id
        )
        db.session.add(light)
        db.session.commit()
        return redirect(url_for('builder_home'))
    return render_template('builder_upload.html', form=form)

@app.route('/builder_likes')
def builder_likes():
    user = User.query.filter_by(username=session['username']).first()
    liked_lights = Light.query.filter_by(builder_id=user.id).all()
    return render_template('builder_likes.html', liked_lights=liked_lights)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
