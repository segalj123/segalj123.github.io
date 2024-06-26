# your_app/users/routes.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from your_app import db, bcrypt
from your_app.models import User, Light
from your_app.users.forms import RegistrationForm, LoginForm, UpdateAccountForm

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if user.is_first_login:
                user.is_first_login = False
                db.session.commit()
                show_popup = True
            else:
                show_popup = False
            if user.user_type == 'designer':
                return redirect(url_for('users.pick_categories', show_popup=show_popup))
            elif user.user_type == 'seller':
                return redirect(url_for('users.upload', show_popup=show_popup))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

@users.route("/pick_categories")
@login_required
def pick_categories():
    if current_user.user_type == 'designer':
        show_popup = request.args.get('show_popup', False)
        return render_template('pick_categories.html', title='Pick Categories', show_popup=show_popup)
    else:
        return redirect(url_for('main.home'))

@users.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    if current_user.user_type == 'seller':
        show_popup = request.args.get('show_popup', False)
        # Upload light logic here
        return render_template('upload.html', title='Upload Light', show_popup=show_popup)
    else:
        return redirect(url_for('main.home'))
