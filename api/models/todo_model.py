"""Todo model module."""
from api import db

from ..models import project_model


class Todo(db.Model):
    """Todo model."""

    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)

    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project = db.relationship(
        project_model.Project, backref=db.backref("todo", lazy="dynamic")
    )
