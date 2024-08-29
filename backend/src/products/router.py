# is a core of each module with all the endpoints

from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import ProductBase
from src.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.products.services import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id,
)

router = APIRouter()


@router.post("/products/", response_model=ProductBase)
async def create_product(product: ProductBase, db: AsyncSession = Depends(get_db)):
    """
    # Create a new product.

        Args:
            product (ProductBase): The product data to be created.
            db (AsyncSession, optional): The database session. Defaults to Depends(get_db).

        Returns:
            The created product.
    """
    db_product = await create_product(db, product)
    if db_product is None:
        raise HTTPException(status_code=400, detail="Product already exists")
    return db_product


@router.get("/products/")
async def get_products(db: AsyncSession = Depends(get_db)):
    """
    # Get all products from the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.

        Returns:
        - result: The result of getting all products from the database.
    """
    result = await get_all_products(db)
    return result


@router.get("/products/{product_id}")
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Get a product by its ID.

        Parameters:
            - product_id (int): The ID of the product.
            - db (AsyncSession, optional): The database session. Defaults to the result of the `get_db` dependency.

        Returns:
            - product: The product with the specified ID.

        Raises:
            - HTTPException: If the product with the specified ID is not found (status code 404).
    """
    product = await get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.patch("/products/{product_id}")
async def update_product(
    product_id: int, product: ProductBase, db: AsyncSession = Depends(get_db)
):
    """
    # Update a product by its ID.

        Parameters:
            - product_id (int): The ID of the product.
            - product (ProductBase): The updated product data.
            - db (AsyncSession, optional): The database session. Defaults to the result of the `get_db` dependency.

        Returns:
            - product: The updated product.

        Raises:
            - HTTPException: If the product with the specified ID is not found (status code 404).
    """
    updated_product = await update_product_by_id(db, product_id, product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    """
    # Delete a product by its ID.

        Parameters:
            - product_id (int): The ID of the product.
            - db (AsyncSession, optional): The database session. Defaults to the result of the `get_db` dependency.

        Returns:
            - product: The deleted product.

        Raises:
            - HTTPException: If the product with the specified ID is not found (status code 404).
    """
    deleted_product = await delete_product_by_id(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product
