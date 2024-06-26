from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from your_app import db, bcrypt
from your_app.models import User
from your_app.users.forms import RegistrationForm, LoginForm, CategoryForm
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, user_type=form.user_type.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        if user.user_type == 'designer':
            return redirect(url_for('users.select_categories'))
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route('/check_username', methods=['POST'])
def check_username():
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return jsonify({'is_available': user is None})

@users.route('/check_email', methods=['POST'])
def check_email():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    return jsonify({'is_available': user is None})

@users.route('/select_categories', methods=['GET', 'POST'])
def select_categories():
    form = CategoryForm()
    if form.validate_on_submit():
        # Handle the form submission logic here
        return redirect(url_for('main.swipe'))
    return render_template('select_categories.html', title='Select Categories', form=form)
