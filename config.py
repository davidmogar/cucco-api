class BaseConfig(object):
    """Parent configuration class."""
    CSRF_ENABLED = True
    DEBUG = False
    RATELIMIT_HEADERS_ENABLED = True

class DevelopmentConfig(BaseConfig):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(BaseConfig):
    """Configurations for Testing.

    This Testing configuration uses a separate database.
    """
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
