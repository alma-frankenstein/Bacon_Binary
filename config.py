import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
<<<<<<< HEAD
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'totally_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
=======
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'totally_secret' # needed for flask-wtf?
>>>>>>> origin/master
