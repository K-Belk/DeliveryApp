# for db models


from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base


class User(Base):
    """
    The `User` class is a model that represents the `users` table in the database.

        Attributes:
            id (int): The ID of the user.
            username (str): The username of the user.
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            is_active (bool): The status of the user.
            created_at (DateTime): The date and time the user was created.
            updated_at (DateTime): The date and time the user was last updated.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active})>"

    def __str__(self):
        return f"User: {self.username}, Email: {self.email}, Active: {self.is_active}"
