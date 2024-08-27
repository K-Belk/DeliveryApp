#  for pydantic models


from pydantic import BaseModel, Field

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

    quantity_scheduled: int
    quantity_delivered: int | None = None
    delivery_location_id: int
    product_id: int
    quantity_scheduled: int  # this is the quantity that was scheduled to be delivered, determined by the past deliveries of the product type to the location
    quantity_delivered: int | None = (
        None  # this is the quantity that was actually delivered, will be updated by the delivery person
    )
    delivery_date: str | None = None
    delivery_time: str | None = None
    delivery_notes: str | None = Field(None, max_length=300)
    delivery_status: str | None = None
    delivered_by: str | None = None
