"""Project model module."""
from api import db

from .employee_model import Employee

employee_project = db.Table(
    "employee_project",
    db.Column(
        "project_id",
        db.Integer,
        db.ForeignKey("project.id"),
        primary_key=True,
        nullable=False,
    ),
    db.Column(
        "employee_id",
        db.Integer,
        db.ForeignKey("employee.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Project(db.Model):
    """Project model."""

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    employees = db.relationship(
        Employee, secondary="employee_project", back_populates="projects"
    )
