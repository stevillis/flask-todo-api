"""Employee service module."""

from typing import List

from api import db

from ..entities.employee_entity import Employee as EmployeeEntity
from ..models.employee_model import Employee as EmployeeModel


def create_employee(employee: EmployeeEntity) -> EmployeeModel:
    """Create employee service."""
    employee_db = EmployeeModel(name=employee.name, birth_date=employee.birth_date)

    db.session.add(employee_db)
    db.session.commit()

    return employee_db


def get_employees() -> List[EmployeeModel]:
    """Get employees service."""
    return EmployeeModel.query.all()


def get_employee_by_pk(pk):
    """Get employee by pk service."""
    return EmployeeModel.query.filter_by(id=pk).first()


def update_employee(employee_db, new_employee):
    """Update employee service."""
    employee_db.name = new_employee.name
    employee_db.birth_date = new_employee.birth_date
    db.session.commit()


def delete_employee(employee):
    """Delete employee service."""
    db.session.delete(employee)
    db.session.commit()
