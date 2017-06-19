from flask import Blueprint

api = Blueprint('v1', __name__, url_prefix='/api/v1')

from app.api.v1 import routes
