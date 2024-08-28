# is a core of each module with all the endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.auth.schemas import UserCreate, UserResponse, Token
from src.auth.services import create_user, login_for_access_token
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
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
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
async def get_users(db: AsyncSession = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    result = await db.execute(select(current_user))
    users = result.scalars().all()

    return users


# # Path to get a specific user
# @router.get("/users/{user_id}")
# async def get_user(user_id: int):
#     return {"message": f"User with id {user_id} returned successfully"}

# # Path to update a user
# @router.put("/users/{user_id}")
# async def update_user(user_id: int):
#     return {"message": f"User with id {user_id} updated successfully"}

# # Path to delete a user
# @router.delete("/users/{user_id}")
# async def delete_user(user_id: int):
#     return {"message": f"User with id {user_id} deleted successfully"}