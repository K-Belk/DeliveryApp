"""

This module contains non-business logic functions for authentication.

Functions:
- normalize_response(response: dict) -> dict: Normalizes the response by removing any sensitive information.
- enrich_data(data: dict) -> dict: Enriches the data by adding additional information.
"""

from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from src.auth.constants import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify the password against the hashed password.

        Args:
            plain_password (str): The plain password.
            hashed_password (str): The hashed password.

        Returns:
            bool: True if the password is valid, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Get the hashed password.

        Args:
            password (str): The password.

        Returns:
            str: The hashed password.
    """
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create an access token.

        Args:
            data (dict): The data to encode.
            expires_delta (timedelta, optional): The expiration time. Defaults to None.

        Returns:
            str: The access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt