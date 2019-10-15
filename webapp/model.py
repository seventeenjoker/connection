from flask_sqlalchemy import SQLAlchemy #ForeignKey #, Table, Column, Integer
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)
        login = db.Column(db.String(50), unique=True, nullable=False)
        password = db.Column(db.String(100), nullable=False)
        persons = db.relationship("Person", backref="user")

        def __repr__(self):
            return f'<User id {self.id}>'

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
            pass

class PythagoreanSquare(db.Model):
        __tablename__ = 'pythagoreanSquare'
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
            pass