"""User model module."""
from passlib.hash import pbkdf2_sha256

from api import db


class User(db.Model):
    """User model."""

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def encrypt_password(self):
        """Encrypt password using sha256."""
        self.password = pbkdf2_sha256.hash(self.password)
