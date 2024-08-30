#  for pydantic models


from pydantic import BaseModel, HttpUrl, validator
from typing import Optional


class DeliveryLocationBase(BaseModel):
    """
    Represents the base schema for a delivery location.
        Attributes:
            name (str): The name of the delivery location.
            street (str): The street address of the delivery location.
            suite (str, optional): The suite number of the delivery location. Defaults to None.
            city (str): The city of the delivery location.
            state (str): The state of the delivery location.
            postal_code (int): The postal code of the delivery location.
            notes (str, optional): Additional notes about the delivery location. Defaults to None.
            delivery_zone (str, optional): The delivery zone of the location. Defaults to None.
    """
    

    name: str
    street: str
    suite: str | None = None
    city: str
    state: str
    postal_code: int
    notes: str | None = None
    delivery_zone: str | None = None


class DeliveryLocationResponse(DeliveryLocationBase):
    """
    Represents a delivery location response.
        Attributes:
            id (int | None): The ID of the delivery location.
            place_id (str | None): The place ID of the delivery location.
            latitude (float | None): The latitude of the delivery location.
            longitude (float | None): The longitude of the delivery location.
            business_type (str | None): The business type of the delivery location.
            phone (str | None): The phone number of the delivery location.
            hours (str | None): The hours of operation of the delivery location.
            website (str | None): The website URL of the delivery location.
            photo_url (str | None): The photo URL of the delivery location.
        Config:
            from_attributes (bool): Indicates whether to load attributes from the class attributes.
    """
 

    id: int | None = None
    place_id: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    business_type: str | None = None
    phone: str | None = None
    hours: str | None = None
    website: str | None = None
    photo_url: str| None = None

    class Config:
        from_attributes = True
