#  router dependencies

from typing import Optional
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select 
from src.products.models import Product
from src.products.schemas import ProductBase, ProductResponse
from src.database import get_db


async def check_product_exist(product: ProductBase, db: AsyncSession = Depends(get_db)) -> Optional[None]:
    """
    Check if a product already exists in the database.
    
        Parameters:
            - db (AsyncSession): The database session.
            - product (ProductBase): The product to check.
        
        Returns:
            - Optional[Product]: The existing product if found, otherwise None.
        
        Raises:
            - HTTPException: If the product already exists in the database.
    """
    result = await db.execute(
        select(Product).filter(Product.name == product.name, Product.edition == product.edition)
    )
    existing_product = result.scalars().first()
    
    if existing_product:
        # Convert the existing product to a response model or dictionary
        existing_product_data = ProductResponse.from_orm(existing_product).dict()
        raise HTTPException(
            status_code=400, 
            detail={
                "message": "Product already exists",
                "existing_product": existing_product_data
            }
        )
    return None