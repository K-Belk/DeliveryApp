#  module specific business logic

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.products.models import Product
from src.products.schemas import ProductBase
from typing import Optional
from datetime import timedelta


async def create_product(db: AsyncSession, product: ProductBase) -> Product:
    """
    # Create a new product and stores it in the database.

        Args:
            db (AsyncSession): The database session.
            product (ProductBase): The product data.

        Returns:
            Product: The created product.
    """

    new_product = Product(
        name=product.name,
        description=product.description,
        edition=product.edition,
        image=product.image,
        notes=product.notes,
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


async def get_all_products(db: AsyncSession) -> Optional[Product]:
    """
    Retrieves all products from the database.

        Args:
            db (AsyncSession): The database session.

        Returns:
            Product: The product.
    """

    result = await db.execute(select(Product))
    return result.scalars().all()


async def get_product_by_id(db: AsyncSession, product_id: int) -> Optional[Product]:
    """
    Retrieves a product from the database by id.

        Args:
            db (AsyncSession): The database session.
            product_id (int): The id of the product.

        Returns:
            Product: The product.
    """

    result = await db.execute(select(Product).filter(Product.id == product_id))
    return result.scalars().first()


async def update_product_by_id(
    db: AsyncSession, product_id: int, product: ProductBase
) -> Optional[Product]:
    """
    Updates a product in the database by id.

        Args:
            db (AsyncSession): The database session.
            product_id (int): The id of the product.
            product (ProductBase): The product data.

        Returns:
            Product: The updated product.
    """

    db_product = await db.execute(select(Product).filter(Product.id == product_id))
    if not db_product:
        return None

    for key, value in product.dict().items():
        setattr(db_product, key, value)

    await db.commit()
    await db.refresh(db_product)
    return db_product


async def delete_product_by_id(db: AsyncSession, product_id: int) -> Optional[Product]:
    """
    Deletes a product from the database by id.

        Args:
            db (AsyncSession): The database session.
            product_id (int): The id of the product.

        Returns:
            Product: The deleted product.
    """

    db_product = await db.execute(select(Product).filter(Product.id == product_id))
    if not db_product:
        return None

    await db.delete(db_product)
    await db.commit()
    return db_product
