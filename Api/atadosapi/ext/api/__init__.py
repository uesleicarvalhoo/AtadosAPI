from flask import Flask
from flask_restful import Api

from .resources import (ActionResource, ActionsResource, VoluntaryResource,
                        VolunteersResource)

api = Api()


def init_app(app: Flask) -> None:
    api.add_resource(VolunteersResource, "/api/voluntary/")
    api.add_resource(VoluntaryResource, "/api/voluntary/<int:id>")
    api.add_resource(ActionsResource, "/api/action/")
    api.add_resource(ActionResource, "/api/action/<int:id>")

    api.init_app(app)
