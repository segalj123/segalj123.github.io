from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from your_app import db, bcrypt
from your_app.forms import RegistrationForm, LoginForm, UploadForm, FilterForm
from your_app.models import User, Light
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('main.register'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, user_type=form.user_type.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
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

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/designer_dashboard")
@login_required
def designer_dashboard():
    if current_user.user_type != 'designer':
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home'))
    return render_template('designer_dashboard.html', title='Designer Dashboard')

@main.route("/seller_dashboard")
@login_required
def seller_dashboard():
    if current_user.user_type != 'seller':
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home'))
    return render_template('seller_dashboard.html', title='Seller Dashboard')

@main.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    if current_user.user_type != 'seller':
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home'))
    form = UploadForm()
    if form.validate_on_submit():
        light = Light(
            name=form.name.data,
            category=form.category.data,
            image_file=form.image.data.filename,
            color=form.color.data,
            price=form.price.data,
            min_order_quantity=form.min_order_quantity.data,
            location_type=form.location_type.data,
            designer=current_user
        )
        db.session.add(light)
        db.session.commit()
        flash('Your light has been uploaded!', 'success')
        return redirect(url_for('main.seller_dashboard'))
    return render_template('upload.html', title='Upload Light Image', form=form)

@main.route("/swipe", methods=['GET', 'POST'])
@login_required
def swipe():
    if current_user.user_type != 'designer':
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home'))
    form = FilterForm()
    lights = Light.query
    if form.validate_on_submit():
        if form.category.data:
            lights = lights.filter_by(category=form.category.data)
        if form.color.data:
            lights = lights.filter_by(color=form.color.data)
        if form.min_price.data:
            lights = lights.filter(Light.price >= form.min_price.data)
        if form.max_price.data:
            lights = lights.filter(Light.price <= form.max_price.data)
        if form.min_order_quantity.data:
            lights = lights.filter(Light.min_order_quantity >= form.min_order_quantity.data)
        if form.location_type.data:
            lights = lights.filter_by(location_type=form.location_type.data)
    lights = lights.all()
    return render_template('swipe.html', title='Swipe Lights', form=form, lights=lights)

@main.route("/add_to_wishlist", methods=['POST'])
@login_required
def add_to_wishlist():
    data = request.get_json()
    light_id = data.get('light_id')
    light = Light.query.get_or_404(light_id)
    current_user.wishlist.append(light)
    db.session.commit()
    return jsonify({'message': 'Light added to wishlist'})

@main.route("/wishlist")
@login_required
def wishlist():
    if current_user.user_type != 'designer':
        flash('You do not have access to this page.', 'danger')
        return redirect(url_for('main.home'))
    return render_template('wishlist.html', title='Wishlist', lights=current_user.wishlist)
