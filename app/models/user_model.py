import json

from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from app.database import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(128), nullable=False)
    phone=db.Column(db.String(50), nullable=False)
    role=db.Column(db.String(50), nullable=False)
    
    

    def __init__(self, name, email,password, phone, rol="Customer"):
        self.name=name
        self.email=email
        self.password=generate_password_hash(password)
        self.phone=phone
        self.rol=rol


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def rolll(self, rol):
        return self.rol==rol
