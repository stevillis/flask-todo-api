"""Employee model module."""
from api import db


class Employee(db.Model):
    """Employee model."""

    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
