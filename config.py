import os
from logging.handlers import RotatingFileHandler
import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = logging.DEBUG


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.ERROR


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'development')
    app.config.from_object(config[config_name])
    handler = RotatingFileHandler('hulu_calculator.log', maxBytes=1000000, backupCount=1)
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])