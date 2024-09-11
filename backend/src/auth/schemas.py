#  for pydantic models


from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Represents the base schema for user data shared between different operations.

        Attributes:
            username (str): The username of the user.
            email (EmailStr): The email address of the user.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
    """

    username: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class UserCreate(UserBase):
    """
    Represents the schema for creating a new user, which requires a password.

        Attributes:
            password (str): The password of the user.
    """

    password: str


class UserResponse(UserBase):
    """
    Represents the schema for returning user data from the API, including ID and active status.

        Attributes:
            id (int): The ID of the user.
            is_active (bool): The status of the user.
    """

    id: int | None = None
    is_active: bool

    # The `Config` class provides extra configuration for Pydantic models
    # `orm_mode=True` tells Pydantic to read data even if it is returned as ORM models
    class Config:
        from_attributes = True

class Token(BaseModel):
    """
    Represents the schema for returning JWT tokens after successful login.

        Attributes:
            access_token (str): The access token.
            token_type (str): The token type.
    """

    access_token: str
    token_type: str
    refresh_token: str

class LoginResponse(BaseModel):
    """
    Represents the schema for returning user data and JWT tokens after successful login.

        Attributes:
            user (UserResponse): The user data.
            access_token (str): The access token.
            token_type (str): The token type.
    """

    user: UserResponse
    token: Token