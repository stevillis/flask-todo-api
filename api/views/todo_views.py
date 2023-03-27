"""Todo views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import todo_entity
from ..schemas import todo_schema
from ..services import todo_service


class TodoList(Resource):
    """Todo class based views."""

    def get(self):
        """Sample of GET request."""
        return "Hello, world!"

    def post(self):
        """Create Todo view."""
        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
        print(validate)
        if validate:
            return make_response(jsonify(validate), 400)

        title = request.json["title"]
        description = request.json["description"]
        expiration_date = request.json["expiration_date"]

        new_todo = todo_entity.Todo(
            title=title,
            description=description,
            expiration_date=expiration_date,
        )

        todo_db = todo_service.create_todo(new_todo)

        return make_response(ts.jsonify(todo_db), 201)


api.add_resource(TodoList, "/todos")
