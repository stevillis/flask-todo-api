"""Todo schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import todo_model


class TodoSchema(ma.ModelSchema):
    """Todo schema class."""

    class Meta:
        """Todo schema meta definitions."""

        model = todo_model.Todo
        fields = ("id", "title", "description", "expiration_date")

    title = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
    expiration_date = ma_fields.Date(required=True)
