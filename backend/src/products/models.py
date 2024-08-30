# for db models

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    """
    # Represents a product.

        Attributes:
            id (int): The unique identifier of the product.
            name (str): The name of the product.
            description (str): The description of the product.
            edition (str): The edition of the product.
            image (str): The image path of the product (nullable).
            notes (str): Additional notes about the product (nullable).
            created_at (datetime): The timestamp when the product was created.
            updated_at (datetime): The timestamp when the product was last updated.

        Methods:
            __repr__(): Returns a string representation of the product.
            __str__(): Returns a string representation of the product.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    edition = Column(String, index=True)
    image = Column(String, nullable=True , index=True)
    notes = Column(String, nullable=True , index=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship to deliveries
    deliveries = relationship("Delivery", back_populates="product")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, edition={self.edition})>"

    def __str__(self):
        return f"Product: {self.name}, Edition: {self.edition}"