import os


class Config:
    """
    Common Config Class(Parent)
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    APP_SETTINGS = os.getenv('APP_SETTINGS')
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentEnv(Config):
    """
    Development environment configuration
    """
    DEBUG = True

class TestingEnv(Config):
    """
    Testing environment configuration
    """
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('TEST_DB')

class ProductionEnv(Config):
    """
    Production environment configuration
    """
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'production': ProductionEnv
}
