#  module specific business logic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth.models import User
from src.auth.utils import get_password_hash, verify_password, create_access_token
from src.auth.schemas import UserCreate
from datetime import timedelta
from src.auth.constants import ACCESS_TOKEN_EXPIRE_MINUTES

async def get_user(db: AsyncSession, id: int):
    """
    Get a user by ID.

        Args:
            db (AsyncSession): The database session.
            id (int): The ID of the user.

        Returns:
            User: The user.
    """
    async with db() as session:
        result = await session.execute(select(User).filter(User.id == id))
        return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str):
    """
    Get a user by email.

        Args:
            db (AsyncSession): The database session.
            email (str): The email of the user.

        Returns:
            User: The user.
    """
    async with db() as session:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

# async def create_user(db: AsyncSession, user: UserCreate) -> User:
    