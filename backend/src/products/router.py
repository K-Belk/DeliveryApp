# is a core of each module with all the endpoints

from fastapi import APIRouter
from .schemas import ProductBase

router = APIRouter()

# Path to create a new porduct
@router.post("/products/", response_model=ProductBase)
async def create_product(product: ProductBase):
    return {"message": "Product created successfully"}

# Path to get all products
@router.get("/products/")
async def get_products():
    return {"message": "All products returned successfully"}

# Path to get a specific product
@router.get("/products/{product_id}")
async def get_product(product_id: int):
    return {"message": f"Product with id {product_id} returned successfully"}

# Path to update a product
@router.put("/products/{product_id}")
async def update_product(product_id: int):
    return {"message": f"Product with id {product_id} updated successfully"}

# Path to delete a product
@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return {"message": f"Product with id {product_id} deleted successfully"}