import json
from os.path import abspath, dirname, join


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    PROJECT_DIR = dirname(dirname(abspath(__file__)))
    DATA_FILE = join(PROJECT_DIR, "restaurants.json")
    with open(DATA_FILE, 'r') as f:
        DATA = json.load(f)


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
