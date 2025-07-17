from flask import render_template
from flask_restful import Resource
from .import api


class IndexApi(Resource):
    def get(self):
        return render_template("index.html")

api.add_resource(IndexApi, "/")