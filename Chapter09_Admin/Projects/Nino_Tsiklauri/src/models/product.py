from src.ext import db
from src.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)

    def __repr__(self):
        return self.name
