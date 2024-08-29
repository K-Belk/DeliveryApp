# is a core of each module with all the endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth.schemas import UserCreate, UserResponse, Token
from src.auth.services import (
    create_user,
    login_for_access_token,
    get_all_users,
    get_user_by_username,
    get_user_by_email,
    update_user_by_username,
    delete_user_by_username,
)
from src.auth.dependencies import get_current_user
from src.database import get_db

# Create a FastAPI router instance for handling authentication routes
router = APIRouter()


@router.post("/register/", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    # Register a new user.

        Args:
            user (UserCreate): The user data to be registered.
            db (AsyncSession, optional): The database session. Defaults to Depends(get_db).

        Returns:
            The registered user.

        Raises:
            HTTPException: If the user already exists.
    """
    db_user = await create_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user


@router.post("/token/", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    """
    # Authenticate user and generate access token.

        Parameters:
        - form_data (OAuth2PasswordRequestForm): The form data containing the username and password.
        - db (AsyncSession): The database session.

        Returns:
        - str: The access token.

        Raises:
        - HTTPException: If the username or password is incorrect.
    """

    token = await login_for_access_token(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@router.get("/users/")
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    """
    # Get all users.

        Parameters:
        - db (AsyncSession): The database session.
        - current_user (UserResponse): The current user.

        Returns:
        - result: The list of all users.
    """
    result = await get_all_users(db)

    return result


@router.get("/users/{username}", response_model=UserResponse)
async def get_user(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    """
    # Get a specific user by username.

        Parameters:
        - username (str): The username of the user.
        - db (AsyncSession): The database session.
        - current_user (UserResponse): The current user.

        Returns:
        - UserResponse: The user.
    """
    user = await get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/users/{username}", response_model=UserResponse)
async def update_user(
    username: str,
    user_data: UserResponse,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    async def update_user(
        username: str,
        user_data: UserResponse,
        db: AsyncSession = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user),
    ):
        """
        # Update a user's information.

            Args:
                username (str): The username of the user to update.
                user_data (UserResponse): The updated user data.
                db (AsyncSession, optional): The database session. Defaults to Depends(get_db).
                current_user (UserResponse, optional): The current authenticated user. Defaults to Depends(get_current_user).

            Returns:
                UserResponse: The updated user data.

            Raises:
                HTTPException: If the user is not found.
        """

    user = await update_user_by_username(db, username, user_data.dict())
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{username}")
async def delete_user(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
):
    """
    # Delete a user by username.

        Parameters:
            username (str): The username of the user to delete.
            db (AsyncSession): The database session.
            current_user (UserResponse): The current user.

        Returns:
            UserResponse: The deleted user.
    """
    user = await delete_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
