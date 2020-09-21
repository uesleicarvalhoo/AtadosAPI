from typing import List

from atadosapi.ext.db.models import Actions, Voluntary
from flask import request
from flask_restful import Resource


class VolunteersResource(Resource):
    def get(self) -> List[dict]:
        return [voluntary.to_dict() for voluntary in Voluntary.query.all()]

    def post(self) -> [dict, int]:
        status = 200
        data = request.json

        if data is None:
            response = {
                "success": False,
                "message": "Informe os dados do voluntario através de um JSON",
            }

        else:
            voluntary = Voluntary()
            voluntary.populate_obj(data)
            response = voluntary.save()

            if not response["success"]:
                status = 400

        return response, status


class VoluntaryResource(Resource):
    def get(self, id: int) -> dict:
        voluntary = Voluntary.get(id)
        if voluntary is None:
            response = {"success": False, "message": "Voluntario não cadastrado"}

        else:
            response = {"success": True, "voluntary": voluntary.to_dict()}

        return response

    def delete(self, id: int) -> [dict]:
        voluntary = Voluntary.get(id)

        if voluntary is None:
            response = {"success": False, "message": "Voluntario não cadastrado"}

        else:
            response = voluntary.delete()

        return response

    def put(self, id: int) -> dict:
        data = request.json
        voluntary = Voluntary.get(id)

        if voluntary is None:
            response = {"success": False, "message": "Voluntario não cadastrado"}

        elif data is None:
            response = {
                "success": False,
                "message": "Informe os dados que devem ser atualizados via JSON",
            }

        else:
            voluntary.populate_obj(data)
            response = voluntary.save()

        return response


class ActionsResource(Resource):
    def get(self) -> List[dict]:
        return [action.to_dict() for action in Actions.query.all()]

    def post(self) -> [dict, int]:
        status = 200
        data = request.json

        if data is None:
            response = {
                "success": False,
                "message": "Informe os dados da ação através de um JSON",
            }

        else:
            action = Actions()
            action.populate_obj(data)
            response = action.save()

            if not response["success"]:
                status = 400

        return response, status


class ActionResource(Resource):
    def get(self, id: int) -> dict:
        action = Actions.get(id)
        if action is None:
            response = {"success": False, "message": "Ação não cadastrada"}

        else:
            response = {"success": True, "action": action.to_dict()}

        return response

    def delete(self, id: int) -> [dict]:
        action = Actions.get(id)

        if action is None:
            response = {"success": False, "message": "Ação não cadastrada"}

        else:
            response = action.delete()

        return response

    def put(self, id: int) -> dict:
        data = request.json
        action = Actions.get(id)

        if action is None:
            response = {"success": False, "message": "Ação não cadastrado"}

        elif data is None:
            response = {
                "success": False,
                "message": "Informe os dados que devem ser atualizados via JSON",
            }

        else:
            action.populate_obj(data)
            response = action.save()

        return response
