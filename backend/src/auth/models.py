# for db models


from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base


class User(Base):
    """
    Represents the User model.

        Attributes:
            id (int): The ID of the user.
            username (str): The username of the user.
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.
            full_name (str, optional): The full name of the user. Defaults to None.
            is_active (bool): The status of the user.
            created_at (DateTime): The date and time the user was created.
            updated_at (DateTime): The date and time the user was last updated.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())