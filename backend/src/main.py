from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as auth_router
from src.deliveries.router import router as delivery_router
from src.delivery_locations.router import router as delivery_location_router
from src.products.router import router as product_router
from fastapi.security import OAuth2PasswordBearer

from src.delivery_locations.utils import GoogleCalls

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins, modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(auth_router)
app.include_router(delivery_router)
app.include_router(delivery_location_router)
app.include_router(product_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Delivery API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}


