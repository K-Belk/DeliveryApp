# for db models

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from src.database import Base
from sqlalchemy.orm import relationship

class DeliveryLocation(Base):
    """
    Represents a delivery location.
        Attributes:
            id (int): The unique identifier of the delivery location.
            name (str): The name of the delivery location.
            street (str): The street address of the delivery location.
            suite (str): The suite number of the delivery location.
            city (str): The city of the delivery location.
            state (str): The state of the delivery location.
            postal_code (int): The postal code of the delivery location.
            notes (str): Additional notes about the delivery location.
            business_type (str): The type of business at the delivery location.
            delivery_zone (str): The delivery zone of the location.
            latitude (float): The latitude coordinate of the delivery location.
            longitude (float): The longitude coordinate of the delivery location.
            phone (str): The phone number of the delivery location.
            hours (str): The operating hours of the delivery location.
            url (str): The URL of the delivery location.
            photo_url (str): The URL of the photo of the delivery location.
            created_at (datetime): The timestamp when the delivery location was created.
            updated_at (datetime): The timestamp when the delivery location was last updated.
    """
    __tablename__ = "delivery_locations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    street = Column(String, nullable=False)
    suite = Column(String)
    city = Column(String, nullable=False, index=True)
    state = Column(String, nullable=False, index=True)
    postal_code = Column(Integer, index=True)
    notes = Column(String)
    business_type = Column(String, index=True)
    delivery_zone = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    phone = Column(String)
    hours = Column(String)
    url = Column(String)
    photo_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    deliveries = relationship("Delivery", back_populates="location")

    def __repr__(self):
        return f"<DeliveryLocation(id={self.id}, name={self.name}, address={self.street}, city={self.city}, state={self.state})>"

    def __str__(self):
        return f"Delivery Location: {self.name},address={self.street}, City: {self.city}, State: {self.state}"
