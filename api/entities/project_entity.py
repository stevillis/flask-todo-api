"""Project entity module."""

from typing import List

from ..models.employee_model import Employee


class Project:
    """Project entity."""

    def __init__(self, name: str, description: str, employees: List[Employee]) -> None:
        self.__name = name
        self.__description = description
        self.__employees = employees

    @property
    def name(self):
        """name getter."""
        return self.__name

    @name.setter
    def name(self, name):
        """name setter."""
        self.__name = name

    @property
    def description(self):
        """Description getter."""
        return self.__description

    @description.setter
    def description(self, description):
        """Description setter."""
        self.__description = description

    @property
    def employees(self):
        """Employees getter."""
        return self.__employees

    @employees.setter
    def employees(self, employees):
        """Employees setter."""
        self.__employees = employees
