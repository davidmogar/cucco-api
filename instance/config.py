import os

class Config(object):
    """Parent configuration class."""
    CSRF_ENABLED = True
    DEBUG = False
    LOG_FOLDER = os.getenv('LOG_FOLDER')
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing.

    This Testing configuration uses a separate database.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    TESTING = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'testing': TestingConfig,
}
