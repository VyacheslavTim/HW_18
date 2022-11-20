from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie import movie_ns
from views.director import director_ns
from views.genre import genre_ns


def register_extensions(app):
    api = Api(app)
    db.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def start_up_app(config_file):
    app = Flask(__name__)
    app.config.from_object(config_file)
    register_extensions(app)
    return app


app = start_up_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=False)
