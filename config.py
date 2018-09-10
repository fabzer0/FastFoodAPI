"""
Contains various settings for each process of development
"""


class Config:
    """Base class with all the constant config variables"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "jfsahe8r934"

class Testing(Config):
    """Contains additional config variables required during testing"""
    DEBUG = True
    TESTING = True

class Development(Config):
    """Contains additional config variables required during development"""
    DEBUG = True

class Production(Config):
    """
    Contains configuration variables required during Production
    """
    DEBUG = False
    TESTING = False
