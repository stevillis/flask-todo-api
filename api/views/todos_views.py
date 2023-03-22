from flask_restful import Resource
from api import api


class TodoList(Resource):
    def get(self):
        return "Hello, world!"


api.add_resource(TodoList, "/todos")
