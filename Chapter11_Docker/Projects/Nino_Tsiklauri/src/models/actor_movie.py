from src.ext import db
from src.models.base import BaseModel


### MANY TO MANY RELATIONSHIP ###
class Actor(BaseModel):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    movies = db.relationship("Movie", back_populates="actors", secondary="actor_movie")


class ActorMovie(BaseModel):
    __tablename__ = "actor_movie"
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))


class Movie(BaseModel):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genre = db.Column(db.String)
    rating = db.Column(db.Float)

    actors = db.relationship("Actor", back_populates="movies", secondary="actor_movie")
