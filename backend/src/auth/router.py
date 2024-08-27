# is a core of each module with all the endpoints

from fastapi import APIRouter
from .schemas import UserBase, UserCreate, UserResponse, Token

router = APIRouter()


# Path to create a new user
@router.post("/users/")
async def create_user():
    return {"message": "User created successfully"}

# Path to get all users
@router.get("/users/")
async def get_users():
    return {"message": "All users returned successfully"} 

# Path to get a specific user
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"message": f"User with id {user_id} returned successfully"}

# Path to update a user
@router.put("/users/{user_id}")
async def update_user(user_id: int):
    return {"message": f"User with id {user_id} updated successfully"}

# Path to delete a user
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"User with id {user_id} deleted successfully"}