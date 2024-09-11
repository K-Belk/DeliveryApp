# is a core of each module with all the endpoints

from fastapi import APIRouter, status, Depends
from .schemas import DeliveryLocationBase, DeliveryLocationResponse
from typing import Optional
from src.database import AsyncSession, get_db
from .services import (
    create_new_delivery_location,
    get_all_delivery_locations,
    get_delivery_location_by_id,
    update_delivery_location_by_id,
    delete_delivery_location_by_id,
)
from .dependencies import check_location_exist
from .models import DeliveryLocation

router = APIRouter()


@router.post("/delivery_location", response_model=DeliveryLocationResponse)
async def create_delivery_location(
    location: DeliveryLocationBase,
    db: AsyncSession = Depends(get_db),
    _: Optional[DeliveryLocation] = Depends(check_location_exist),
):
    """
    # Create a new delivery location.

        Parameters:
            - location: The delivery location information.
            - db: The database session.

        Returns:
            - The created delivery location.

    """
    return await create_new_delivery_location(db, location)


@router.get("/delivery_locations")
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


@router.patch(
    "/delivery_location/{location_id}", response_model=DeliveryLocationResponse
)
async def update_delivery_location(
    location_id: int,
    location: DeliveryLocationResponse,
    db: AsyncSession = Depends(get_db),
):
    """
    # Update a delivery location by its ID.

        Parameters:
            - location_id (int): The ID of the delivery location to update.
            - location (DeliveryLocationBase): The updated delivery location data.
            - db (AsyncSession): The database session.

        Returns:
            - The updated delivery location.
    """
    return await update_delivery_location_by_id(db, location_id, location)


@router.delete("/delivery_location/{location_id}")
async def delete_delivery_location(
    location_id: int, db: AsyncSession = Depends(get_db)
):
    """
    # Delete a delivery location by ID.

        Parameters:
            - location_id (int): The ID of the delivery location.
            - db (AsyncSession): The asynchronous session to connect to the database.

        Returns:
            - DeliveryLocation: The deleted delivery location.
    """
    return await delete_delivery_location_by_id(db, location_id)
