from flask_restx import Resource, Namespace

from container import genre_service as service
from dao.models.genre import GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        data = service.get_all()
        return GenreSchema(many=True).dump(data), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        data = service.get_one(gid)
        return GenreSchema().dump(data), 200
    