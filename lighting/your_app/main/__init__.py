from flask import Blueprint

main = Blueprint('main', __name__)

from your_app.main import routes
