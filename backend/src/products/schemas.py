#  for pydantic models

from pydantic import BaseModel, HttpUrl

class ProductBase(BaseModel):
    """
    # Represents the base schema for a product.

        Attributes:
            name (str): The name of the product.
            description (str, optional): The description of the product. Defaults to None.
            edition (str, optional): The edition of the product. Defaults to None.
            image (str, optional): The image URL of the product. Defaults to None.
            notes (str, optional): Additional notes about the product. Defaults to None.
    """
    name: str
    description: str | None = None
    edition: str 
    image: HttpUrl | None = None
    notes: str | None = None

class ProductResponse(ProductBase):
    """
    # Represents the response schema for a product.

        Attributes:
            id (int): The unique identifier of the product.
    """
    id: int

    class Config:
        from_attributes = True
