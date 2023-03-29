"""Project schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import project_model


class ProjectSchema(ma.SQLAlchemySchema):
    """Project schema class."""

    class Meta:
        """Project schema meta definitions."""

        model = project_model.Project
        fields = ("id", "name", "description")
        load_model = True

    name = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
