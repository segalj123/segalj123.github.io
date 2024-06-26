from your_app import db
from your_app.models import User, Light, LightImage
from flask_bcrypt import generate_password_hash
import json

def add_initial_data():
    # Add initial users with hashed passwords
    hashed_password1 = generate_password_hash('password123').decode('utf-8')
    hashed_password2 = generate_password_hash('password123').decode('utf-8')
    user1 = User(username='segalj', email='jsegal1@babson.edu', password=hashed_password1, user_type='designer')
    user2 = User(username='seller1', email='seller1@example.com', password=hashed_password2, user_type='seller')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Add initial lights
    light1 = Light(name='Elegant Chandelier', category='Chandelier', image_files=json.dumps(['chandelier1.jpg', 'chandelier2.jpg']), color='Gold', price=500, min_order_quantity=1, location_type='House', user_id=user2.id)
    light2 = Light(name='Modern Pendant', category='Pendant', image_files=json.dumps(['pendant1.jpg', 'pendant2.jpg']), color='Silver', price=200, min_order_quantity=5, location_type='Apartment', user_id=user2.id)
    light3 = Light(name='Classic Ceiling Light', category='Ceiling Light', image_files=json.dumps(['ceiling1.jpg', 'ceiling2.jpg']), color='White', price=150, min_order_quantity=10, location_type='Office', user_id=user2.id)
    db.session.add(light1)
    db.session.add(light2)
    db.session.add(light3)
    db.session.commit()

    print("Initial data added successfully.")
