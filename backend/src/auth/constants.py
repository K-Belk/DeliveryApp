#  module specific constants and error codes

import os
from dotenv import load_dotenv

# Load environment variables from a .env file, if you are using one
load_dotenv()

# Define the secret key used for JWT encoding/decoding
# It's recommended to store this in an environment variable for security
SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")

# Define the algorithm used to sign the JWT tokens
ALGORITHM = "HS256"

# Define the access token expiration time in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # or any value that suits your application

# Define the refresh token expiration time in days
REFRESH_TOKEN_EXPIRE_DAYS = 7  # or any value that suits your application