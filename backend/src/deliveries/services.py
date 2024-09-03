#  module specific business logic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from .models import Delivery
from .schemas import DeliveryBase, DeliveryResponse
from typing import Optional


async def create_new_delivery(
    db: AsyncSession, delivery: DeliveryBase
) -> DeliveryResponse:
    """
    Create a new delivery.

        Args:
            db (AsyncSession): The database db.
            delivery (DeliveryBase): The delivery data.

        Returns:
            DeliveryResponse: The created delivery data.
    """
    new_delivery = Delivery(**delivery.dict())

    db.add(new_delivery)
    print(f"new_delivery: {new_delivery.delivery_date}")
    await db.commit()
    await db.refresh(new_delivery)
    return DeliveryResponse(**new_delivery.__dict__)


async def get_all_deliveries(db: AsyncSession) -> Optional[DeliveryResponse]:
    """
    Get all deliveries.

        Args:
            db (AsyncSession): The database db.

        Returns:
            DeliveryResponse: The delivery data.
    """
    result = await db.execute(select(Delivery).options(joinedload(Delivery.user), joinedload(Delivery.product), joinedload(Delivery.location)))
    return result.scalars().all()


async def get_delivery_by_id(
    db: AsyncSession, delivery_id: int
) -> Optional[DeliveryResponse]:
    """
    Get delivery by ID.

        Parameters:
            - db: AsyncSession - The async db object.
            - delivery_id: int - The ID of the delivery.

        Returns:
            - Optional[DeliveryResponse] - The delivery response object if found, otherwise None.
    """
    result = await db.execute(select(Delivery).options(joinedload(Delivery.user), joinedload(Delivery.product), joinedload(Delivery.location)).filter(Delivery.id == delivery_id))
    return result.scalars().first()


async def get_deliveries_by_user(
    db: AsyncSession, user_id: int
) -> Optional[DeliveryResponse]:
    """
    Get deliveries by user.

        Parameters:
            - db: AsyncSession - The async db object.
            - user_id: int - The ID of the user.

        Returns:
            - Optional[DeliveryResponse] - The delivery response object if found, otherwise None.
    """
    result = await db.execute(select(Delivery).filter(Delivery.user_id == user_id))
    return result.scalars().all()


async def get_deliveries_by_location(
    db: AsyncSession, location_id: int
) -> Optional[DeliveryResponse]:
    """
    Get deliveries by location.

        Parameters:
            - db: AsyncSession - The async db object.
            - location_id: int - The ID of the location.

        Returns:
            - Optional[DeliveryResponse] - The delivery response object if found, otherwise None.
    """
    result = await db.execute(
        select(Delivery).options(joinedload(Delivery.user), joinedload(Delivery.product), joinedload(Delivery.location)).filter(Delivery.location_id == location_id)
    )
    return result.scalars().all()


async def get_deliveries_by_product(
    db: AsyncSession, product_id: int
) -> Optional[DeliveryResponse]:
    """
    Get deliveries by product.

        Parameters:
            - db: AsyncSession - The async db object.
            - product_id: int - The ID of the product.

        Returns:
            - Optional[DeliveryResponse] - The delivery response object if found, otherwise None.
    """
    result = await db.execute(
        select(Delivery).options(joinedload(Delivery.user), joinedload(Delivery.product), joinedload(Delivery.location)).filter(Delivery.product_id == product_id)
    )
    return result.scalars().all()


async def update_delivery_by_id(
    db: AsyncSession, delivery_id: int, delivery: DeliveryBase
) -> Optional[DeliveryResponse]:
    """
    Update a delivery in the database.

        Args:
            db (AsyncSession): The database session.
            delivery_id (int): The ID of the delivery to update.
            delivery (DeliveryBase): The updated delivery information.

        Returns:
            Optional[DeliveryResponse]: The updated delivery response if successful, None otherwise.
    """
    db_delivery = await get_delivery_by_id(db, delivery_id)

    if not db_delivery:
        return None

    for key, value in delivery.dict().items():
        setattr(db_delivery, key, value)

    await db.commit()
    await db.refresh(db_delivery)
    return DeliveryResponse(**db_delivery.__dict__)


async def delete_delivery_by_id(
    db: AsyncSession, delivery_id: int
) -> Optional[DeliveryResponse]:
    """
    Delete a delivery from the database.

        Args:
            db (AsyncSession): The database session.
            delivery_id (int): The ID of the delivery to delete.

        Returns:
            Optional[DeliveryResponse]: The deleted delivery, wrapped in a `DeliveryResponse` object,
            or `None` if the delivery does not exist.
    """

    db_delivery = await get_delivery_by_id(db, delivery_id)

    if not db_delivery:
        return None

    await db.delete(db_delivery)
    await db.commit()
    return db_delivery
