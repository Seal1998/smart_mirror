import os
class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/test.db'.format(os.getcwd())