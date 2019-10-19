import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'db.db')

SECRET_KEY = "lisedgtbhrunhgiqeru7345y923n#$%^&*(djfkbg)"