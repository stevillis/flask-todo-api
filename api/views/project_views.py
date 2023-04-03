"""Project views module."""

from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api

from ..entities import project_entity
from ..models.project_model import Project
from ..pagination import paginate
from ..schemas import project_schema
from ..services import project_service


def get_project_fields(req):
    """Get project fields from request."""
    name = req.json["name"]
    description = req.json["description"]
    employees = req.json["employees"]

    return name, description, employees


class ProjectList(Resource):
    """Project class based views without parameter."""

    @jwt_required()
    def get(self):
        """Get Projects view."""
        # projects = project_service.get_projects()
        ps = project_schema.ProjectSchema(many=True)

        # return make_response(ps.jsonify(projects), 200)
        return paginate(Project, ps)

    @jwt_required()
    def post(self):
        """Create Project view."""
        ps = project_schema.ProjectSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, employees = get_project_fields(request)

        new_project = project_entity.Project(
            name=name, description=description, employees=employees
        )

        project_db = project_service.create_project(new_project)

        project_db.employees = [employee.id for employee in project_db.employees]
        return make_response(ps.jsonify(project_db), 201)


class ProjectDetail(Resource):
    """Project class based views with parameter."""

    @jwt_required()
    def get(self, pk):
        """Get project by pk view."""
        project = project_service.get_project_by_pk(pk)
        if not project:
            return make_response(jsonify("Project not found!"), 404)

        ps = project_schema.ProjectSchema()
        return make_response(ps.jsonify(project), 200)

    @jwt_required()
    def put(self, pk):
        """Update project view."""
        project_db = project_service.get_project_by_pk(pk)
        if not project_db:
            return make_response(jsonify("Project not found!"), 404)

        ps = project_schema.ProjectSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, description, employees = get_project_fields(request)

        new_project = project_entity.Project(
            name=name, description=description, employees=employees
        )

        project_service.update_project(project_db, new_project)
        updated_project = project_service.get_project_by_pk(pk)

        return make_response(ps.jsonify(updated_project), 200)

    @jwt_required()
    def delete(self, pk):
        """Delete project view."""
        project = project_service.get_project_by_pk(pk)
        if not project:
            return make_response(jsonify("Project not found!"), 404)

        project_service.delete_project(project)
        return make_response("", 204)


api.add_resource(ProjectList, "/projects")
api.add_resource(ProjectDetail, "/projects/<int:pk>")
