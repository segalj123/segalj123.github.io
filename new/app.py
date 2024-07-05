import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from forms import LightUploadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
db = SQLAlchemy(app)

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    light_id = db.Column(db.Integer, db.ForeignKey('light.id'), nullable=False)

class SeenLight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    light_id = db.Column(db.Integer, db.ForeignKey('light.id'), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = LightUploadForm()
    if form.validate_on_submit():
        light = Light(name=form.name.data, category=form.category.data, image_file=form.image_file.data.filename)
        db.session.add(light)
        db.session.commit()
        flash('Light has been uploaded!', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html', form=form)

@app.route('/swipe')
def swipe():
    lights = Light.query.all()
    return render_template('swipe.html', lights=lights)

@app.route('/swipe_action', methods=['POST'])
def swipe_action():
    data = request.json
    user_id = data['user_id']
    light_id = data['light_id']
    action = data['action']

    if action == 'like':
        wishlist = Wishlist(user_id=user_id, light_id=light_id)
        db.session.add(wishlist)
    seen_light = SeenLight(user_id=user_id, light_id=light_id)
    db.session.add(seen_light)
    db.session.commit()
    return {'status': 'success'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
