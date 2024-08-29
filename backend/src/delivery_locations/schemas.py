#  for pydantic models


from pydantic import BaseModel, HttpUrl


class DeliveryLocationBaseIn(BaseModel):
    """
    Represents the base input schema for a delivery location.

        Attributes:
            name (str): The name of the delivery location.
            street (str): The street address of the delivery location.
            suite (str, optional): The suite number of the delivery location. Defaults to None.
            city (str): The city of the delivery location.
            state (str): The state of the delivery location.
            postal_code (int): The postal code of the delivery location.
            notes (str, optional): Additional notes about the delivery location. Defaults to None.
            business_type (str, optional): The type of business at the delivery location. Defaults to None.
            delivery_zone (str, optional): The delivery zone of the delivery location. Defaults to None.
    """

    name: str
    street: str
    suite: str | None = None
    city: str
    state: str
    postal_code: int
    notes: str | None = None
    business_type: str | None = None
    delivery_zone: str | None = None


class DeliveryLocationBaseOut(DeliveryLocationBaseIn):
    """
    Represents the base output schema for a delivery location.

        Attributes:
            location_id (int): The ID of the delivery location.
            latitude (float): The latitude of the delivery location.
            longitude (float): The longitude of the delivery location.
            phone (str): The phone number of the delivery location.
            hours (str, optional): The hours of operation for the delivery location. Defaults to None.
            url (HttpUrl, optional): The URL of the delivery location. Defaults to None.
            photo_url (HttpUrl, optional): The photo URL of the delivery location. Defaults to None.
    """

    id: int
    latitude: float | None = None
    longitude: float | None = None
    phone: str | None = None
    hours: str | None = None
    url: HttpUrl | None = None
    photo_url: HttpUrl | None = None

    class Config:
        from_attributes = True