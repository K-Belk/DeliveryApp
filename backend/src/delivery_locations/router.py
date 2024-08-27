# is a core of each module with all the endpoints

from fastapi import APIRouter, status
from .schemas import DeliveryLocationBaseIn, DeliveryLocationBaseOut

router = APIRouter()


# Path to create a delivery location
@router.post(
    "/delivery_location/",
    response_model=DeliveryLocationBaseOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_delivery_location(location: DeliveryLocationBaseIn):
    """
    # Create a new delivery location

        Function:

            1. Takes in a new delivery location with the provided information.
            2. Searches Google API for the latitude, longitude, phone number, hours of operation, and URL of the delivery location.
            3. Creates the delivery location in the database.
            4. Returns the created delivery location.

        Args:

            location (DeliveryLocationBaseIn): The delivery location to create.
                name (str): The name of the delivery location.
                street (str): The street address of the delivery location.
                suite (str, optional): The suite number of the delivery location. Defaults to None.
                city (str): The city of the delivery location.
                state (str): The state of the delivery location.
                postal_code (int): The postal code of the delivery location.
                notes (str, optional): Additional notes about the delivery location. Defaults to None.
                business_type (str, optional): The type of business at the delivery location. Defaults to None.
                delivery_zone (str, optional): The delivery zone of the delivery location. Defaults to None.

        Returns:

            location (DeliveryLocationBaseOut): The created delivery location.
                location_id (int): The ID of the delivery location.
                name (str): The name of the delivery location.
                street (str): The street address of the delivery location.
                suite (str, optional): The suite number of the delivery location. Defaults to None.
                city (str): The city of the delivery location.
                state (str): The state of the delivery location.
                postal_code (int): The postal code of the delivery location.
                notes (str, optional): Additional notes about the delivery location. Defaults to None.
                business_type (str, optional): The type of business at the delivery location. Defaults to None.
                delivery_zone (str, optional): The delivery zone of the delivery location. Defaults to None.
                latitude (float): The latitude of the delivery location.
                longitude (float): The longitude of the delivery location.
                phone (str): The phone number of the delivery location.
                hours (str, optional): The hours of operation for the delivery location. Defaults to None.
                url (HttpUrl, optional): The URL of the delivery location. Defaults to None.
    """
    return location  # {"message": "Delivery location created successfully"}


# Path to get all delivery locations, returns a list of all delivery locations
@router.get("/delivery_location/")
async def get_delivery_locations():
    return {"message": "All delivery locations returned successfully"}


# Path to get a specific delivery location
@router.get("/delivery_location/{location_id}")
async def get_delivery_location(location_id: int):
    return {"message": f"Delivery location with id {location_id} returned successfully"}


# Path to update a delivery location
@router.patch(
    "/delivery_location/{location_id}", response_model=DeliveryLocationBaseOut
)
async def update_delivery_location(location: DeliveryLocationBaseOut):
    """
    # Update a delivery location

        Function:

            1. Takes in a delivery location ID and the updated information for the delivery location.
            2. Retrieves the delivery location from the database.
            3. Updates the delivery location with the new information.
            4. Updates the delivery location in the database.
            5. Returns the updated delivery location.

        Args:

            location (DeliveryLocationBaseOut): The updated delivery location.
                location_id (int): The ID of the delivery location.
                name (str): The name of the delivery location.
                street (str): The street address of the delivery location.
                suite (str, optional): The suite number of the delivery location. Defaults to None.
                city (str): The city of the delivery location.
                state (str): The state of the delivery location.
                postal_code (int): The postal code of the delivery location.
                notes (str, optional): Additional notes about the delivery location. Defaults to None.
                business_type (str, optional): The type of business at the delivery location. Defaults to None.
                delivery_zone (str, optional): The delivery zone of the delivery location. Defaults to None.
                latitude (float): The latitude of the delivery location.
                longitude (float): The longitude of the delivery location.
                phone (str): The phone number of the delivery location.
                hours (str, optional): The hours of operation for the delivery location. Defaults to None.
                url (HttpUrl, optional): The URL of the delivery location. Defaults to None.

        Returns:

            updated_location (DeliveryLocationBaseOut): The updated delivery location.
                location_id (int): The ID of the delivery location.
                name (str): The name of the delivery location.
                street (str): The street address of the delivery location.
                suite (str, optional): The suite number of the delivery location. Defaults to None.
                city (str): The city of the delivery location.
                state (str): The state of the delivery location.
                postal_code (int): The postal code of the delivery location.
                notes (str, optional): Additional notes about the delivery location. Defaults to None.
                business_type (str, optional): The type of business at the delivery location. Defaults to None.
                delivery_zone (str, optional): The delivery zone of the delivery location. Defaults to None.
                latitude (float): The latitude of the delivery location.
                longitude (float): The longitude of the delivery location.
                phone (str): The phone number of the delivery location.
                hours (str, optional): The hours of operation for the delivery location. Defaults to None.
                url (HttpUrl, optional): The URL of the delivery location. Defaults to None.
    """
    stored_location = get_delivery_location(location.location_id)
    update_data = location.dict(exclude_unset=True)
    updated_location = stored_location.copy(update=update_data)
    # update the delivery location in the database

    return updated_location  # {"message": f"Delivery location with id {location_id} updated successfully"}


# Path to delete a delivery location
@router.delete("/delivery_location/{location_id}")
async def delete_delivery_location(location_id: int):
    return {"message": f"Delivery location with id {location_id} deleted successfully"}
