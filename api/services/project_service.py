"""Project service module."""

from typing import List

from api import db

from ..entities.project_entity import Project as ProjectEntity
from ..models.project_model import Project as ProjectModel
from ..services.employee_service import get_employee_by_pk


def create_project(project: ProjectEntity) -> ProjectModel:
    """Create project service."""
    project_db = ProjectModel(name=project.name, description=project.description)
    for employee_pk in project.employees:
        employee_db = get_employee_by_pk(employee_pk)
        project_db.employees.append(employee_db)

    db.session.add(project_db)
    db.session.commit()

    return project_db


def get_projects() -> List[ProjectModel]:
    """Get projects service."""
    return ProjectModel.query.all()


def get_project_by_pk(pk):
    """Get project by pk service."""
    return ProjectModel.query.filter_by(id=pk).first()


def update_project(project_db, new_project):
    """Update project service."""
    project_db.name = new_project.name
    project_db.description = new_project.description
    project_db.employees = []

    for employee_pk in new_project.employees:
        employee_db = get_employee_by_pk(employee_pk)
        project_db.employees.append(employee_db)

    db.session.commit()


def delete_project(project):
    """Delete project service."""
    db.session.delete(project)
    db.session.commit()
