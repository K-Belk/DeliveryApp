# Backend API

This is the backend API for the DeliveryApp project. It is built using FastAPI and provides endpoints for managing products.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- PostgreSQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DeliveryApp.git
   cd DeliveryApp/backend

2. Create a virtual environment and activate it:
  python3 -m venv venv
  source venv/bin/activate

3. pip install -r requirements.txt

4. Create a .env file in the backend directory with the following content:

  DATABASE_URL={your database URL}
  SECRET_KEY={your secret key}
  POSTGRES_USER={your username}
  POSTGRES_PASSWORD={your password}
  POSTGRES_DB={database name}

## Running the Application

1. Start the PostgreSQL database using Docker Compose:
  docker compose up -d

2. API Endpoints

Create a New Product
- URL: /products/
- Method: POST
- Request Body: ProductBase
- Response: {"message": "Product created successfully"}
Get All Products
-URL: /products/
-Method: GET
-Response: {"message": "All products returned successfully"}
-Get a Specific Product
URL: /products/{product_id}
Method: GET
Path Parameters: product_id (int)
Response: {"message": "Product with id {product_id} returned successfully"}
Update a Product
URL: /products/{product_id}
Method: PATCH
Path Parameters: product_id (int)
Response: {"message": "Product with id {product_id} updated successfully"}
Delete a Product
URL: /products/{product_id}
Method: DELETE
Path Parameters: product_id (int)
Response: {"message": "Product with id {product_id} deleted successfully"}
Project Structure
License
This project is licensed under the MIT License. See the LICENSE file for more details.

```

