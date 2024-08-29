# is a core of each module with all the endpoints

from fastapi import APIRouter, status, Depends
from .schemas import DeliveryLocationBaseIn, DeliveryLocationBaseOut
from typing import Optional
from src.database import AsyncSession, get_db
from src.delivery_locations.services import create_new_delivery_location, get_all_delivery_locations, get_delivery_location_by_id

router = APIRouter()



@router.post(
    "/delivery_location/",
    response_model=DeliveryLocationBaseOut
)
async def create_delivery_location(location: DeliveryLocationBaseIn, db: AsyncSession = Depends(get_db)):
    """
    # Create a new delivery location.

        Parameters:
            - location: The delivery location information.
            - db: The database session.

        Returns:
            - The created delivery location.

    """
    return await create_new_delivery_location(db, location)

@router.get("/delivery_locations/")
async def get_delivery_locations(db: AsyncSession = Depends(get_db)):
    """
    # Get all delivery locations from the database.

        Parameters:
            - db (AsyncSession): The asynchronous session to connect to the database.

        Returns:
            - List[DeliveryLocation]: A list of delivery locations.
    """
    return await get_all_delivery_locations(db)

@router.get("/delivery_location/{location_id}")
async def get_delivery_location(location_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Get a delivery location by ID.

        Parameters:
            - location_id (int): The ID of the delivery location.
            - db (AsyncSession): The asynchronous session to connect to the database.

        Returns:
            - DeliveryLocation: The delivery location.
    """
    return await get_delivery_location_by_id(db, location_id)


# Path to update a delivery location
@router.patch("/delivery_location/{location_id}", response_model=DeliveryLocationBaseOut)
async def update_delivery_location(location: DeliveryLocationBaseOut):
    return# {"message": f"Delivery location with id {location_id} updated successfully"}


# Path to delete a delivery location
@router.delete("/delivery_location/{location_id}")
async def delete_delivery_location(location_id: int):
    return {"message": f"Delivery location with id {location_id} deleted successfully"}
