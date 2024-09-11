#  for pydantic models


from pydantic import BaseModel, Field
from src.auth.schemas import UserResponse
from src.products.schemas import ProductResponse
from src.delivery_locations.schemas import DeliveryLocationResponse

# base class for deliveries, will be used to create pydantic model for deliveries during scheduling. Then later, the delivery person will update the delivery status and quantity delivered in the database


class DeliveryBase(BaseModel):
    """
    Represents the base schema for a delivery.

        Attributes:
            delivery_location_id (int): The ID of the delivery location.
            product_id (int): The ID of the product.
            quantity_scheduled (int): The quantity that was scheduled to be delivered, determined by the past deliveries of the product type to the location.
            quantity_delivered (int, optional): The quantity that was actually delivered, will be updated by the delivery person.
            delivery_date (str, optional): The date of the delivery.
            delivery_time (str, optional): The time of the delivery.
            delivery_notes (str, optional): Additional notes for the delivery.
            delivery_status (str, optional): The status of the delivery.
            delivered_by (str, optional): The name of the person who delivered the product.
    """

    user_id: UserResponse | None = None
    product_id: ProductResponse
    location_id: DeliveryLocationResponse
    quantity_scheduled: int
    delivery_status: str | None = None
    quantity_delivered: int | None = None
    delivery_date: str | None = None
    delivery_notes: str | None = Field(None, max_length=300)

class DeliveryResponse(DeliveryBase):
    """
    Represents the schema for returning delivery data from the API.

        Attributes:
            id (int): The ID of the delivery.
    """

    id: int

    class Config:
        from_attributes = True