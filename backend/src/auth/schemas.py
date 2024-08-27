#  for pydantic models


from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Represents the base schema for a user.

        Attributes:
            username (str): The username of the user.
            email (EmailStr): The email address of the user.
            full_name (str, optional): The full name of the user. Defaults to None.
    """

    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    """
    Represents the schema for creating a user.

        Attributes:
            password (str): The password of the user.
    """

    password: str


class UserResponse(UserBase):
    """
    Represents the schema for a user response.

        Attributes:
            id (int): The ID of the user.
            is_active (bool): The status of the user.
    """

    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    """
    Represents the schema for a token.

        Attributes:
            access_token (str): The access token.
            token_type (str): The token type.
    """

    access_token: str
    token_type: str