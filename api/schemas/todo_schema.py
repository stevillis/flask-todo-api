"""Todo schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import todo_model


class TodoSchema(ma.SQLAlchemySchema):
    """Todo schema class."""

    class Meta:
        """Todo schema meta definitions."""

        model = todo_model.Todo
        fields = ("id", "title", "description", "expiration_date", "project", "_links")
        load_model = True

    title = ma_fields.String(required=True)
    description = ma_fields.String(required=True)
    expiration_date = ma_fields.Date(required=True)
    project = ma_fields.String(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("tododetail", values=dict(pk="<id>")),
            "put": ma.URLFor("tododetail", values=dict(pk="<id>")),
            "delete": ma.URLFor("tododetail", values=dict(pk="<id>")),
        }
    )
