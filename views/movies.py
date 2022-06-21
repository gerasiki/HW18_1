from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.models.movie import MovieSchema
from marshmallow import ValidationError

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        condition = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }
        all_movies = movie_service.get_all(condition)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        args = request.json
        movie = movie_service.create(args)
        return '', 201, {'location': f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        data = movie_service.get_one(mid)
        result = MovieSchema().dump(data)
        return result, 200

    def put(self, mid):
        try:
            data = request.json
            if 'id' not in data:
                data['id'] = mid
            return movie_service.update(data), 204
        except ValidationError as e:
            return {'errors': e.normalized_messages()}, 400

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
