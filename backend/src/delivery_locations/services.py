#  module specific business logic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.delivery_locations.models import DeliveryLocation
from src.delivery_locations.schemas import (
    DeliveryLocationBaseIn,
    DeliveryLocationBaseOut,
)
from typing import Optional


async def create_new_delivery_location(
    db: AsyncSession, location: DeliveryLocationBaseIn
) -> DeliveryLocationBaseOut:
    """
    # Create a new delivery location and stores it in the database.

        Args:
            db (AsyncSession): The database session.
            location (DeliveryLocationBaseIn): The delivery location data.

        Returns:
            DeliveryLocationBaseOut: The created delivery location.
    """
    new_location = DeliveryLocation()

    for key, value in location.dict().items():
        setattr(new_location, key, value)
    
    db.add(new_location)
    await db.commit()
    await db.refresh(new_location)
    return new_location

async def get_all_delivery_locations(
    db: AsyncSession,
) -> Optional[DeliveryLocationBaseOut]:
    """
    Retrieves all delivery locations from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            DeliveryLocationBaseOut: The delivery location.
    """

    result = await db.execute(select(DeliveryLocation))
    return result.scalars().all()

async def get_delivery_location_by_id(
    db: AsyncSession, location_id: int
) -> Optional[DeliveryLocationBaseOut]:
    """
    Retrieves a delivery location from the database by id.

        Args:
            db (AsyncSession): The database session.
            location_id (int): The id of the delivery location.

        Returns:
            DeliveryLocationBaseOut: The delivery location.
    """

    result = await db.execute(
        select(DeliveryLocation).where(DeliveryLocation.id == location_id)
    )
    return result.scalars().first()

async def update_delivery_location_by_id(
    db: AsyncSession, location_id: int, location: DeliveryLocationBaseOut
) -> Optional[DeliveryLocationBaseOut]:
    """
    Updates a delivery location in the database by id.

        Args:
            db (AsyncSession): The database session.
            location_id (int): The id of the delivery location.
            location (DeliveryLocationBaseOut): The delivery location data.

        Returns:
            DeliveryLocationBaseOut: The updated delivery location.
    """

    db_location = await get_delivery_location_by_id(db, location_id
    )

    if not db_location:
        return None

    for key, value in location.dict().items():
        setattr(db_location, key, value)

    await db.commit()
    await db.refresh(db_location)
    return db_location


async def delete_delivery_location_by_id(
    db: AsyncSession, location_id: int
) -> Optional[DeliveryLocationBaseOut]:
    """
    Deletes a delivery location from the database by id.

        Args:
            db (AsyncSession): The database session.
            location_id (int): The id of the delivery location.

        Returns:
            DeliveryLocationBaseOut: The deleted delivery location.
    """

    db_location = await get_delivery_location_by_id(db, location_id
    )

    if not db_location:
        return None

    await db.delete(db_location)
    await db.commit()
    return db_location
