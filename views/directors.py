from flask_restx import Resource, Namespace

from container import director_service as service
from dao.models.director import DirectorSchema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        data = service.get_all()
        return DirectorSchema(many=True).dump(data), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        data = service.get_one(did)
        return DirectorSchema().dump(data), 200
