from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/swipe')
def swipe():
    return render_template('swipe.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')
