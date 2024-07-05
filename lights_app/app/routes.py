from flask import render_template, request, redirect, url_for, jsonify
from app import db
from app.models import Light

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        finish = request.form['finish']
        style = request.form['style']
        color = request.form['color']
        price = request.form['price']
        company = request.form['company']

        new_light = Light(name=name, category=category, finish=finish, style=style, color=color, price=price, company=company)
        db.session.add(new_light)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('upload.html')

@app.route('/swipe', methods=['GET'])
def swipe():
    lights = Light.query.all()
    return render_template('swipe.html', lights=lights)

@app.route('/wishlist/<int:light_id>', methods=['POST'])
def wishlist(light_id):
    light = Light.query.get_or_404(light_id)
    light.wishlist_count += 1
    db.session.commit()
    return jsonify({'success': True, 'wishlist_count': light.wishlist_count})
