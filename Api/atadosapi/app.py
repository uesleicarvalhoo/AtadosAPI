from atadosapi.ext import config
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    config.init_app(app)

    return app
