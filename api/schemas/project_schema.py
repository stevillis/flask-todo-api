"""Project schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import project_model
from ..schemas import employee_schema, todo_schema


class ProjectSchema(ma.SQLAlchemySchema):
    """Project schema class."""

    class Meta:
        """Project schema meta definitions."""

        model = project_model.Project
        fields = ("id", "name", "description", "todos", "employees")
        load_model = True

    name = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
    todos = ma_fields.List(ma_fields.Nested(todo_schema.TodoSchema, only=["id"]))
    # employees = ma_fields.List(ma_fields.Nested(employee_schema.EmployeeSchema, only=["id"]))
