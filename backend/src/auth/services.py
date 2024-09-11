#  module specific business logic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth.models import User
from src.auth.utils import get_password_hash, verify_password, create_access_token
from src.auth.schemas import UserCreate, LoginResponse
from datetime import timedelta
from src.auth.constants import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from typing import Optional

async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """
    # Create a new user and stores it in the database.

        Args:
            db (AsyncSession): The database session.
            user (UserCreate): The user data.

        Returns:
            User: The created user.
    """
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_username(db: AsyncSession, username: str) -> Optional[User]:
    """
    Retrieves a user from the database by username.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user.

        Returns:
            User: The user.
    """
    
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """
    # Retrieves a user from the database by email.

        Args:
            db (AsyncSession): The database session.
            email (str): The email of the user.

        Returns:
            User: The user.
    """
    async with db() as session:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

async def get_all_users(db: AsyncSession) -> list[User]:
    """
    # Retrieves all users from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            list[User]: A list of users.
    """
    
    result = await db.execute(select(User))
    return result.scalars().all()

async def authenticate_user(db: AsyncSession, username: str, password: str) -> Optional[User]:
    """
    # Authenticate a user by verifying the provided password.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User: The authenticated user.
    """
    user = await get_user_by_username(db, username)
    if user and verify_password(password, user.hashed_password):
        return user
    return None
    
async def login_for_access_token(db: AsyncSession, username: str, password: str):
    """
    # Authenticates the user with the provided username and password and generates an access token for a user upon successful authentication.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            dict: A dictionary containing the access token and token type.

        Raises:
            None

    """
    user = await authenticate_user(db, username, password)
    if not user:
        return None
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = create_access_token(
        data={"sub": user.username}, expires_delta=refresh_token_expires
    )
    
    token_data = {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}

    return LoginResponse(user=user, token=token_data)

async def update_user_by_username(db: AsyncSession, username: str, user_data: dict) -> User:
    """
    # Update a user by their username.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user to update.
            user_data (dict): The updated user data.

        Returns:
            User: The updated user object.

    """
    ...
    db_user = await get_user_by_username(db, username)
    if not db_user:
        return None

    for key, value in user_data.items():
        if user_data[key] != None:
            setattr(db_user, key, value)

    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user_by_username(db: AsyncSession, username: str) -> User:
    """
    # Delete a user by their username.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user to delete.

        Returns:
            User: The deleted user object.

    """
    db_user = await get_user_by_username(db, username)
    if not db_user:
        return None

    await db.delete(db_user)
    await db.commit()
    return db_user