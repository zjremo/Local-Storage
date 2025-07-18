from flask import current_app
from flask_restful import Resource
from . import api


class IndexApi(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "Welcome to the Service API",
            "APPName": current_app.config["APPNAME"],
        }


api.add_resource(IndexApi, "/")
