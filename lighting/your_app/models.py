from lighting.your_app.users import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    user_type = db.Column(db.String(10), nullable=False)
    is_first_login = db.Column(db.Boolean, nullable=False, default=True)  # New field
    lights = db.relationship('Light', backref='owner', lazy=True)
    messages = db.relationship('Message', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    min_order_quantity = db.Column(db.Integer, nullable=False)
    location_type = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    images = db.relationship('LightImage', backref='light', lazy=True)

    def __repr__(self):
        return f"Light('{self.name}', '{self.category}', '{self.color}', '{self.price}', '{self.min_order_quantity}', '{self.location_type}')"

class LightImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    light_id = db.Column(db.Integer, db.ForeignKey('light.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"LightImage('{self.image_file}')"

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    light_id = db.Column(db.Integer, db.ForeignKey('light.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Wishlist('{self.user_id}', '{self.light_id}', '{self.timestamp}')"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Message('{self.sender_id}', '{self.recipient_id}', '{self.timestamp}')"
