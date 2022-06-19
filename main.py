from flask import Flask
from flask_restx import Api

from config import Config
from database import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.app_context().push()

    return app


def configure_app(app: Flask):
    db.init_app(app)
    db.create_all()
    api = Api(app, prefix='/api', doc='/docs')
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_ = create_app()
    configure_app(app_)
    app_.run()
