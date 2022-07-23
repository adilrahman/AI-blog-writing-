from distutils.command.config import config
import os
from pickle import TRUE

OPENAI_API_KEY = key = os.environ.get('OPENAI_API_KEY')


class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    SECREY_KEY = ""



config = {
    "development" : DevelopmentConfig,
    "testing" : DevelopmentConfig,
    "production" : DevelopmentConfig
}