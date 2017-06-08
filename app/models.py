from flask_login import UserMixin

from app import db

class User(db.Model, UserMixin):
    """This class represents a user of the api."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(64), unique=True, index=True)
