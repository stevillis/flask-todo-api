"""Todo views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import todo_entity
from ..models.todo_model import Todo
from ..pagination import paginate
from ..schemas import todo_schema
from ..services import project_service, todo_service


def get_todo_fields(req):
    """Get todo fields from request."""
    title = req.json["title"]
    description = req.json["description"]
    expiration_date = req.json["expiration_date"]

    return title, description, expiration_date


class TodoList(Resource):
    """Todo class based views without parameter."""

    def get(self):
        """Get Todos view."""
        # todos = todo_service.get_todos()
        ts = todo_schema.TodoSchema(many=True)

        # return make_response(ts.jsonify(todos), 200)
        return paginate(Todo, ts)

    def post(self):
        """Create Todo view."""
        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        title, description, expiration_date = get_todo_fields(request)

        project = project_service.get_project_by_pk(request.json["project"])
        if project is None:
            return make_response(jsonify("Project not found!"), 404)

        new_todo = todo_entity.Todo(
            title=title,
            description=description,
            expiration_date=expiration_date,
            project=project,
        )

        todo_db = todo_service.create_todo(new_todo)

        return make_response(ts.jsonify(todo_db), 201)


class TodoDetail(Resource):
    """Todo class based views with parameter."""

    def get(self, pk):
        """Get todo by pk view."""
        todo = todo_service.get_todo_by_pk(pk)
        if not todo:
            return make_response(jsonify("Todo not found!"), 404)

        ts = todo_schema.TodoSchema()
        return make_response(ts.jsonify(todo), 200)

    def put(self, pk):
        """Update todo view."""
        todo_db = todo_service.get_todo_by_pk(pk)
        if not todo_db:
            return make_response(jsonify("Todo not found!"), 404)

        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        title, description, expiration_date = get_todo_fields(request)

        project = project_service.get_project_by_pk(request.json["project"])
        if project is None:
            return make_response(jsonify("Project not found!"), 404)

        new_todo = todo_entity.Todo(
            title=title,
            description=description,
            expiration_date=expiration_date,
            project=project,
        )

        todo_service.update_todo(todo_db, new_todo)
        updated_todo = todo_service.get_todo_by_pk(pk)

        return make_response(ts.jsonify(updated_todo), 200)

    def delete(self, pk):
        """Delete todo view."""
        todo = todo_service.get_todo_by_pk(pk)
        if not todo:
            return make_response(jsonify("Todo not found!"), 404)

        todo_service.delete_todo(todo)
        return make_response("", 204)


api.add_resource(TodoList, "/todos")
api.add_resource(TodoDetail, "/todos/<int:pk>")
