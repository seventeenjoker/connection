from model import db
from connection_project.webapp import create_app

db.create_all(app=create_app())