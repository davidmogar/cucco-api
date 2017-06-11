from flask_login import UserMixin

from app.extensions import db

class User(db.Model, UserMixin):
    """This class represents a user of the api."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, id, name, api_key):
        self.id = id
        self.name = name
        self.api_key = api_key
