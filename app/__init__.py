from flask import Flask, jsonify, make_response

from app.api import api_v1, private
from app.extensions import db, limiter, login_manager
from app.models import Role, User, user_datastore

DEFAULT_BLUEPRINTS = [
    api_v1,
    private
]

def create_app(config_object='config.DevelopmentConfig', blueprints=None):
    """Create and configure a new Flask app.

    Attributes:
        config_object: Name of the config to use.
        blueprints: Blueprints to use on this instance.

    Returns:
        A new Flask instance.
    """
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, config_object)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)

    return app

def configure_app(app, config_object):
    """Configure a Flask application using a config object.

    Attributes:
        app: Flask application.
        config_object: Name of the config object to use.
    """
    app.config.from_object(config_object)
    app.config.from_pyfile('config.cfg', silent=True)

def configure_blueprints(app, blueprints):
    """Configure blueprints to use in a Flask application.

    Attributes:
        app: Flask application.
        blueprints: List of blueprints to use.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(app):
    """Configure extensions for a Flask application.

    Attributes:
        app: Flask application.
    """
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    limiter.init_app(app)
    login_manager.init_app(app)

    from flask_cors import CORS, cross_origin
    CORS(app)

def configure_error_handlers(app):
    """Configure error handlers for a Flask application.

    Attributes:
        app: Flask application.
    """
    @app.errorhandler(400)
    def bad_request(e):
        return make_response(jsonify(error=e.description), 400)

    @app.errorhandler(401)
    def bad_request(e):
        return make_response(jsonify(error=e.description), 401)

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
