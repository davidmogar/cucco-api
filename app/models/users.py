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
    """This class represents a user of the API.

    Attributes:
        username: Username of the user.
        email: Email address.
        password: Password of the user.
    """
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
        """Generate a new token.

        Generates a short life new token for the current user.

        Attributes:
            expiration: Time after when the token becomes invalid.
        """
        serializer = Serializer(current_app.config['API_SECRET'],
                                                     expires_in = expiration)
        return serializer.dumps({ 'id': self.id })


    @staticmethod
    def verify_auth_token(token):
        """Verify a given token.

        Verifies a token received as argument and returns the matching user if
        this is found in the database.

        Attributes:
            token: Token to verify.

        Returns:
            A user linked by the token if found.
        """
        data = None
        serializer = Serializer(current_app.config['API_SECRET'])
        user = None

        try:
            data = serializer.loads(token)
        except (BadSignature, SignatureExpired):
            pass # Handled at request loader level

        if data:
            from app.models import user_datastore
            user = user_datastore.find_user(id=data['id'])

        return user
