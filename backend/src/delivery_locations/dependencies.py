#  router dependencies

from typing import Optional
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import DeliveryLocation
from .schemas import DeliveryLocationBaseIn, DeliveryLocationBaseOut
from src.database import get_db

async def check_location_exist(location: DeliveryLocationBaseIn, db: AsyncSession = Depends(get_db)) -> Optional[None]:
    """
    Check if a delivery location already exists in the database.

        Args:
            location (DeliveryLocationBaseIn): The delivery location to check.
            db (AsyncSession, optional): The database session. Defaults to Depends(get_db).

        Returns:
            Optional[None]: Returns None if the delivery location does not exist.

        Raises:
            HTTPException: Raises an exception with status code 400 if the delivery location already exists.
    """
    result = await db.execute(
        select(DeliveryLocation).filter(DeliveryLocation.name == location.name, DeliveryLocation.street == location.street, DeliveryLocation.postal_code == location.postal_code)
    )
    existing_location = result.scalars().first()

    if existing_location:
        # Convert the existing delivery location to a response model or dictionary
        existing_location_data = DeliveryLocationBaseOut.from_orm(existing_location).dict()
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Delivery location already exists",
                "existing_location": existing_location_data
            }
        )
    return None