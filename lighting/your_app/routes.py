from flask import render_template, Blueprint
from your_app.models import Light

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')

@main.route("/swipe")
def swipe():
    lights = Light.query.all()
    return render_template('swipe.html', title='Swipe Lights', lights=lights)
