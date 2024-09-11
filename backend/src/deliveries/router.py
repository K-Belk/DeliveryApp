# is a core of each module with all the endpoints

from fastapi import APIRouter, status, Depends
from .schemas import DeliveryBase
from src.database import get_db, AsyncSession
from .services import (
    create_new_delivery,
    get_all_deliveries,
    get_delivery_by_id,
    get_deliveries_by_user,
    get_deliveries_by_location,
    get_deliveries_by_product,
    update_delivery_by_id,
    delete_delivery_by_id,
)

router = APIRouter()


@router.post("/delivery", response_model=DeliveryBase)
async def create_delivery(delivery: DeliveryBase, db: AsyncSession = Depends(get_db)):
    """
    # Create a new delivery.

        Parameters:
            - delivery: The delivery information.
            - db: The database session.

        Returns:
            - The created delivery.

    """
    return await create_new_delivery(db, delivery)


@router.get("/deliveries", status_code=status.HTTP_200_OK)
async def get_deliveries(db: AsyncSession = Depends(get_db)):
    """
    # Get all deliveries from the database.

        Parameters:
            - db (AsyncSession): The asynchronous session to connect to the database.

        Returns:
            - List[Delivery]: A list of all deliveries.

    """
    return await get_all_deliveries(db)


@router.get("/delivery/{delivery_id}")
async def get_delivery(delivery_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Get a delivery by its ID.

        Parameters:
            - delivery_id (int): The ID of the delivery.
            - db (AsyncSession, optional): The database session. Defaults to the result of the `get_db` function.

        Returns:
            - The delivery with the specified ID.

    """
    return await get_delivery_by_id(db, delivery_id)


@router.get("/deliveries/user/{user_id}")
async def get_delivery_by_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Retrieves a delivery by user ID.

        Parameters:
            - user_id (int): The ID of the user.
            - db (AsyncSession, optional): The database session. Defaults to the result of the get_db function.

        Returns:
            - The delivery associated with the user ID.

    """
    return await get_deliveries_by_user(db, user_id)


@router.get("/deliveries/location/{location_id}")
async def get_delivery_by_location(
    location_id: int, db: AsyncSession = Depends(get_db)
):
    """
    # Retrieves a delivery by its location ID.

        Parameters:
            - location_id (int): The ID of the location.

        Returns:
            - The delivery associated with the given location ID.
    """
    return await get_deliveries_by_location(db, location_id)


@router.get("/deliveries/product/{product_id}")
async def get_delivery_by_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Retrieves the delivery information for a given product.

        Parameters:
            - product_id (int): The ID of the product to retrieve the delivery information for.
            - db (AsyncSession, optional): The database session. Defaults to the result of the `get_db` dependency.

        Returns:
            - The delivery information for the given product.

    """
    return await get_deliveries_by_product(db, product_id)


@router.patch("/deliveries/{delivery_id}")
async def update_delivery(
    delivery_id: int, delivery: DeliveryBase, db: AsyncSession = Depends(get_db)
):
    """
    # Update a delivery by its ID.

        Parameters:
            - delivery_id (int): The ID of the delivery to be updated.
            - delivery (DeliveryBase): The updated delivery information.
            - db (AsyncSession, optional): The database session. Defaults to the session obtained from `get_db` dependency.

        Returns:
            - The updated delivery.

    """
    return await update_delivery_by_id(db, delivery_id, delivery)


@router.delete("/deliveries/{delivery_id}")
async def delete_delivery(delivery_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Delete a delivery by its ID.

        Parameters:
            - delivery_id (int): The ID of the delivery to be deleted.
            - db (AsyncSession): The database session.

        Returns:
            - The result of the delete operation.

    """
    return await delete_delivery_by_id(db, delivery_id)
