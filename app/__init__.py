from flask import Flask, jsonify, make_response

from instance.config import app_config
from app.api import api_v1, private
from app.extensions import db, limiter, login_manager
from app.models import User

DEFAULT_BLUEPRINTS = [
    api_v1,
    private
]

def create_app(config_name='development', blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, config_name)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)
    populate_db(app, config_name)

    return app

def configure_app(app, config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    limiter.init_app(app)
    login_manager.init_app(app)

def configure_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return make_response(jsonify(error=e.description), 400)

    @app.errorhandler(401)
    def bad_request(e):
        return make_response(jsonify(error='unauthorized'), 401)

    @app.errorhandler(404)
    def not_found(e):
        return make_response(jsonify(error='url not found'), 404)

    @app.errorhandler(429)
    def ratelimit_handler(e):
        return make_response(
                jsonify(error='ratelimit exceeded',
                        requests='%s' % e.description),
                429)

    @app.errorhandler(500)
    def not_found(e):
        return make_response(jsonify(error=e.description), 500)

def populate_db(app, config_name):
    if config_name == 'testing':
        with app.app_context():
            user = User.query.get(1)

            if user:
                user.api_key = '1234'
            else:
                db.session.add(User(1, 'admin', '1234'))

            db.session.commit()
