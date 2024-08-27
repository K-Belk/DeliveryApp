# is a core of each module with all the endpoints

from fastapi import APIRouter, status
from .schemas import DeliveryBase

router = APIRouter()


# Path to create a new delivery
@router.post(
    "/deliveries/", response_model=DeliveryBase, status_code=status.HTTP_200_OK
)
async def create_delivery(delivery: DeliveryBase):
    return delivery  # {"message": "Delivery created successfully"}


# Path to get all deliveries
@router.get("/deliveries/", status_code=status.HTTP_200_OK)
async def get_deliveries():
    return {"message": "All deliveries returned successfully"}


# Path to get a specific delivery
@router.get("/deliveries/{delivery_id}")
async def get_delivery(delivery_id: int):
    return {"message": f"Delivery with id {delivery_id} returned successfully"}


#  Path to get a delivery by user
@router.get("/deliveries/user/{user_id}")
async def get_delivery_by_user(user_id: int):
    return {"message": f"Deliveries for user with id {user_id} returned successfully"}


#  Path to get a delivery by location
@router.get("/deliveries/location/{location_id}")
async def get_delivery_by_location(location_id: int):
    return {
        "message": f"Deliveries for location with id {location_id} returned successfully"
    }


#  Path to get a delivery by product
@router.get("/deliveries/product/{product_id}")
async def get_delivery_by_product(product_id: int):
    return {
        "message": f"Deliveries for product with id {product_id} returned successfully"
    }


# Path to update a delivery
@router.put("/deliveries/{delivery_id}")
async def update_delivery(delivery_id: int):
    return {"message": f"Delivery with id {delivery_id} updated successfully"}


# Path to delete a delivery
@router.delete("/deliveries/{delivery_id}")
async def delete_delivery(delivery_id: int):
    return {"message": f"Delivery with id {delivery_id} deleted successfully"}
