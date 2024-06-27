# your_app/main/routes.py

from flask import Blueprint, render_template
from your_app.models import Light

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', title='Home')

@main.route('/swipe')
def swipe():
    lights = Light.query.all()
    return render_template('swipe.html', lights=lights)
