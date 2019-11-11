from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db

class User(db.Model, UserMixin):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        login = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
        is_admin = db.Column(db.Boolean, nullable=False, default=False)
        persons = db.relationship("Person", backref="user")

        def set_password(self, password):
            self.password = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password, password)

        def __repr__(self):
            return f'{self.login}'

class Person(db.Model):
        __tablename__ = 'person'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        last_name = db.Column(db.String, nullable=False)
        first_name = db.Column(db.String, nullable=False)
        datetime_of_birth = db.Column(db.DateTime, nullable=False)
        middle_name = db.Column(db.String)
        pythagorean_square = relationship("PythagoreanSquare", uselist=False, backref="person")

        def __repr__(self):
            return f'<id {self.id}>'

class PythagoreanSquare(db.Model):
        __tablename__ = 'pythagorean_square'
        id = db.Column(db.Integer, primary_key=True)
        person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
        first = db.Column(db.Integer)
        second = db.Column(db.Integer)
        third = db.Column(db.Integer)
        fourth = db.Column(db.Integer)
        fifth = db.Column(db.Integer)
        sixth = db.Column(db.Integer)
        seventh = db.Column(db.Integer)
        eighth = db.Column(db.Integer)
        ninth = db.Column(db.Integer)
        
        def __repr__(self):
            return f'<id {self.id}>'