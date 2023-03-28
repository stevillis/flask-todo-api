"""Todo views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import todo_entity
from ..schemas import todo_schema
from ..services import todo_service


class TodoList(Resource):
    """Todo class based views without parameter."""

    def get(self):
        """Get Todos view."""
        todos = todo_service.get_todos()
        ts = todo_schema.TodoSchema(many=True)

        return make_response(ts.jsonify(todos), 200)

    def post(self):
        """Create Todo view."""
        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
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


class TodoDetail(Resource):
    """Todo class based views with parameter."""

    def get(self, pk):
        """Get todo by pk view."""
        todo = todo_service.get_todo_by_pk(pk)
        if todo:
            ts = todo_schema.TodoSchema()
            return make_response(ts.jsonify(todo), 200)

        return make_response(jsonify("Todo not found!"), 404)


api.add_resource(TodoList, "/todos")
api.add_resource(TodoDetail, "/todos/<int:pk>")
