import uuid

from flask import current_app
from flask_security import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

from app.extensions import db


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

class User(db.Model, UserMixin):
    """This class represents a user of the api."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    active = db.Column(db.Boolean(), default=True)
    api_key = db.Column(db.String(255), nullable=False)

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User({}, {}, username={}): {}>'.format(self.id, self.username, self.email, self.is_autheicated)

    def generate_auth_token(self, expiration = 600):
        serializer = Serializer(current_app.config['API_SECRET'],
                                                     expires_in = expiration)
        return serializer.dumps({ 'id': self.id })


    @staticmethod
    def verify_auth_token(token):
        data = None
        serializer = Serializer(current_app.config['API_SECRET'])

        try:
            data = serializer.loads(token)
        except (BadSignature, SignatureExpired):
            pass # Handled at request loader level

        from app.models import user_datastore
        user = user_datastore.find_user(id=data['id'])

        return user
