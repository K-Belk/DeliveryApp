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
)
from src.auth.dependencies import get_db, get_current_user

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
    Get all users.

        Parameters:
        - db (AsyncSession): The database session.
        - current_user (UserResponse): The current user.

        Returns:
        - result: The list of all users.
    """
    result = await get_all_users(db)

    return result


# Path to get a specific user
@router.get("/users/{username}")
async def get_user(
    username: str,
    db: AsyncSession = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
) -> UserResponse:
    """
    Get a specific user by username.

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


# # Path to update a user
# @router.put("/users/{user_id}")
# async def update_user(user_id: int):
#     return {"message": f"User with id {user_id} updated successfully"}

# # Path to delete a user
# @router.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     return {"message": f"User with id {user_id} deleted successfully"}
