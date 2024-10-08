#  router dependencies

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import async_session, get_db
from src.auth.services import get_user_by_username
from src.auth.schemas import UserResponse
from src.auth.constants import SECRET_KEY, ALGORITHM


# Defines a OAuth2PasswordBearer instance, specifying the tokenUrl as "token"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> UserResponse:
    """
    Asynchronous function that retrieves the current user from the database using the JWT token.

        Args:
            token (str): The token.
            db (AsyncSession): The database session.

        Returns:
            User: The user.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user_by_username(db, username)
    if user is None or not user.is_active:
        raise credentials_exception

    return user