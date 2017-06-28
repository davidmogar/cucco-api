# Flask limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Flask login
from flask import abort, g
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

@login_manager.request_loader
def load_user_from_request(request):
    user = None
    token = request.headers.get('token')

    if token:
        user = User.verify_auth_token(token)
    else:
        api_key = request.headers.get('api_key')

        if api_key:
            user = User.query.filter_by(api_key=api_key).first()

    # Don't wait for the error and abort the request
    if not user:
        abort(400, 'token invalid or expired' if token else 'unauthorized')

    g.user = user

    return user
