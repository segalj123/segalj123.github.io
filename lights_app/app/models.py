from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    finish = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    wishlist_count = db.Column(db.Integer, default=0)
