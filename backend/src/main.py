from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.deliveries.router import router as delivery_router
from src.delivery_locations.router import router as delivery_location_router
from src.products.router import router as product_router
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(auth_router)
app.include_router(delivery_router)
app.include_router(delivery_location_router)
app.include_router(product_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Delivery API"}