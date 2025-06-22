from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.ext import db
from src.models.base import BaseModel


class User (BaseModel, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password = db.Column(db.String)
    profile_image = db.Column(db.String)
    role = db.Column(db.String)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_admin(self):
        return self.role == "Admin"

    #getter
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)