from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/home')
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/swipe')
def swipe():
    lights = Light.query.all()
    return render_template('swipe.html', lights=lights)

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # handle file upload here
        pass
    return render_template('upload.html')
