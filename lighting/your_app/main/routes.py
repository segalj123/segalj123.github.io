from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/swipe')
def swipe():
    # Assuming you have a Light model and you are querying it
    lights = Light.query.all()
    return render_template('swipe.html', lights=lights)
