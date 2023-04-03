"""Employee views module."""

from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entities import employee_entity
from ..models.employee_model import Employee
from ..pagination import paginate
from ..schemas import employee_schema
from ..services import employee_service


def get_employee_fields(req):
    """Get employee fields from request."""
    name = req.json["name"]
    birth_date = req.json["birth_date"]

    return name, birth_date


class EmployeeList(Resource):
    """Employee class based views without parameter."""

    def get(self):
        """Get Employees view."""
        # employees = employee_service.get_employees()
        es = employee_schema.EmployeeSchema(many=True)

        # return make_response(es.jsonify(employees), 200)
        return paginate(Employee, es)

    def post(self):
        """Create Employee view."""
        es = employee_schema.EmployeeSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, birth_date = get_employee_fields(request)

        new_employee = employee_entity.Employee(name=name, birth_date=birth_date)

        employee_db = employee_service.create_employee(new_employee)

        return make_response(es.jsonify(employee_db), 201)


class EmployeeDetail(Resource):
    """Employee class based views with parameter."""

    def get(self, pk):
        """Get employee by pk view."""
        employee = employee_service.get_employee_by_pk(pk)
        if not employee:
            return make_response(jsonify("Employee not found!"), 404)

        es = employee_schema.EmployeeSchema()
        return make_response(es.jsonify(employee), 200)

    def put(self, pk):
        """Update employee view."""
        employee_db = employee_service.get_employee_by_pk(pk)
        if not employee_db:
            return make_response(jsonify("Employee not found!"), 404)

        es = employee_schema.EmployeeSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        name, birth_date = get_employee_fields(request)

        new_employee = employee_entity.Employee(name=name, birth_date=birth_date)

        employee_service.update_employee(employee_db, new_employee)
        updated_employee = employee_service.get_employee_by_pk(pk)

        return make_response(es.jsonify(updated_employee), 200)

    def delete(self, pk):
        """Delete employee view."""
        employee = employee_service.get_employee_by_pk(pk)
        if not employee:
            return make_response(jsonify("Employee not found!"), 404)

        employee_service.delete_employee(employee)
        return make_response("", 204)


api.add_resource(EmployeeList, "/employees")
api.add_resource(EmployeeDetail, "/employees/<int:pk>")
