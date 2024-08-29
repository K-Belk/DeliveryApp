# for db models

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base

class Delivery(Base):
    """
    Represents a delivery.

        Attributes:
            id (int): The unique identifier of the delivery.
            user_id (int): The ID of the user associated with the delivery.
            product_id (int): The ID of the product being delivered.
            location_id (int): The ID of the delivery location.
            status (str): The status of the delivery.
            delivery_date (datetime): The date and time of the delivery.
            created_at (datetime): The date and time when the delivery was created.
            updated_at (datetime): The date and time when the delivery was last updated.
            user (User): The user associated with the delivery.
            product (Product): The product being delivered.
            location (DeliveryLocation): The delivery location.

        Methods:
            __repr__(): Returns a string representation of the delivery.
            __str__(): Returns a string representation of the delivery.
    """
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("delivery_locations.id"), nullable=False)
    status = Column(String, nullable=False)
    delivery_date = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="deliveries")
    product = relationship("Product", back_populates="deliveries")
    location = relationship("DeliveryLocation", back_populates="deliveries")

    def __repr__(self):
        return f"<Delivery(id={self.id}, status={self.status}, delivery_date={self.delivery_date})>"

    def __str__(self):
        return f"Delivery {self.id} - {self.status} on {self.delivery_date}"