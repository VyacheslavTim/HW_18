from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace("genre")


@genre_ns.route("/")
class GenreView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        return result, 200


@genre_ns.route("/")
class GenreView(Resource):
    def get(self, uid):
        genres = genre_service.get_one(uid)
        result = GenreSchema().dump(genres)
        return result, 200
