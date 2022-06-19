from marshmallow import Schema, fields
from database import db
from sqlalchemy.orm import relationship


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)

    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    director = relationship('Director')
    genre = relationship('Genre')


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

