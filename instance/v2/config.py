import os


class Config:
    """
    Common Config Class(Parent)
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    USER = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PWD')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')


class DevelopmentEnv(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    APP_SETTINGS = 'development'
    DB_NAME = os.getenv('DB_NAME')

class TestingEnv(Config):
    """
    Testing environment configuration
    """
    TESTING = True
    DEBUG = True
    DB_NAME = os.getenv('TEST_DB')


class ProductionEnv(Config):
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False
    APP_SETTINGS = os.getenv('FLASK_RELEASE')


app_config = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'production': ProductionEnv
}
