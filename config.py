import logging
from os import path

DEBUG = True
TESTING = False
# sqlite :memory: identifier is the default if no filepath is present
# SQLALCHEMY_DATABASE_URI = 'sqlite://'
# SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = path.join(path.dirname(path.abspath(__file__)), 'logs/app.log')
LOGGING_LEVEL = logging.DEBUG