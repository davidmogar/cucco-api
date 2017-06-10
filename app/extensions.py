# Flask limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Flask login
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

@login_manager.request_loader
def load_user_from_request(request):
    user = None
    api_key = request.headers.get('Authorization')

    if api_key:
        user = User.query.filter_by(api_key=api_key).first()

    return user
