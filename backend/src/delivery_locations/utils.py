# non-business logic functions, e.g. response normalization, data enrichment, etc.

from dotenv import load_dotenv
import os
import googlemaps
from .schemas import DeliveryLocationResponse

# Load the .env file
load_dotenv()

class GoogleCalls:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

    def format_location_base(self, location):
        """
        Formats the given location dictionary into a formatted string.
            Args:
                location (dict): A dictionary containing the location information.
            Returns:
                str: The formatted location string.
        """
        location_base = location['name'] + " " + (location['suite'] + " " if 'suite' in location and location['suite'] else "") + location['city'] + ", " + location['state'] + " " + str(location['postal_code'])
        
        return location_base

    def format_business_hours(self, hours):
        """
        Formats the given business hours list into a formatted string.
            Args:
                hours (list): A list containing the business hours.
            Returns:
                str: The formatted business hours string.
        """
        formatted_hours = ""
        for hour in hours:
            formatted_hours += hour + "\n"
        
        return formatted_hours

    def get_place_id(self, location):
        """
        Retrieves the place ID of a given location.
            Args:
                location (str): The location to retrieve the place ID for.
            Returns:
                str: The place ID of the location.
        """
        place_id = self.gmaps.find_place(location, input_type='textquery')['candidates'][0]['place_id']
        
        return place_id

    def get_location_info(self, location):
        """
        Retrieves information about a delivery location.
            Args:
                location (str): The location to retrieve information for.
            Returns:
                DeliveryLocationResponse: An object containing the information about the delivery location.
            Raises:
                SomeException: If there is an error retrieving the location information.
        """
        
        place_id_response = self.get_place_id(self.format_location_base(location))
        
        place_details = self.gmaps.place(place_id_response)['result']
        
        response = DeliveryLocationResponse(
            place_id=place_details['place_id'],
            name=place_details['name'],
            street=place_details['address_components'][0]['short_name'] + " " + place_details['address_components'][1]['short_name'],
            city=place_details['address_components'][2]['short_name'],
            state=place_details['address_components'][4]['short_name'],
            postal_code=int(place_details['address_components'][6]['short_name']),
            phone=place_details['formatted_phone_number'],
            website=place_details['website'],
            hours=self.format_business_hours(place_details['current_opening_hours']['weekday_text']),
            business_type=place_details['types'][0],
            latitude=float(place_details['geometry']['location']['lat']),
            longitude=float(place_details['geometry']['location']['lng'])        )

        return response
