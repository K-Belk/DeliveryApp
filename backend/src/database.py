# Database connection and session setup

import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create the database async session
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)