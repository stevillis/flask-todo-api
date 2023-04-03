"""Employee schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import employee_model


class EmployeeSchema(ma.SQLAlchemySchema):
    """Employee schema class."""

    class Meta:
        """Employee schema meta definitions."""

        model = employee_model.Employee
        fields = ("id", "name", "birth_date", "projects")
        load_model = True

    name = ma_fields.String(required=True)
    birth_date = ma_fields.Date(required=True)
