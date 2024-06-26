# reset_db.py
from your_app import create_app, db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database has been reset and all tables are recreated.")
