"""Todo service module."""

from api import db

from ..entities.todo_entity import Todo as TodoEntity
from ..models.todo_model import Todo as TodoModel


def create_todo(todo: TodoEntity) -> TodoModel:
    """Create todo service."""
    todo_db = TodoModel(title=todo.title, description=todo.description, expiration_date=todo.expiration_date)

    db.session.add(todo_db)
    db.session.commit()

    return todo_db
