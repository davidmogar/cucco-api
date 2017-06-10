from flask import jsonify, make_response
from flask_api import FlaskAPI

from instance.config import app_config
from app.api import common, private, public
from app.extensions import db, limiter, login_manager

DEFAULT_BLUEPRINTS = [
    common,
    private,
    public
]

def create_app(config_name='development', blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = FlaskAPI(__name__, instance_relative_config=True)
    configure_app(app, config_name)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_error_handlers(app)
    configure_hooks(app)

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

def configure_hooks(app):
    pass

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
