from webapp.model import db
from webapp import create_app

db.create_all(app=create_app())