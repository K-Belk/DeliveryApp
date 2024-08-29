# Database connection and session setup

import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# The DATABASE_URL is an environment variable that contains your database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

# `create_async_engine` is used to create a SQLAlchemy engine with asynchronous capabilities
engine = create_async_engine(DATABASE_URL, echo=True)

# `sessionmaker` creates a configured "session factory" that can generate new `AsyncSession` instances
# `expire_on_commit=False` means that objects will not be expired from the session after committing
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# `declarative_base` is a factory function that constructs a base class for declarative class definitions
Base = declarative_base()


async def get_db():
    """
    Asynchronous function that returns a database session.

        Returns:
            session: An async session object representing a database session.
    """
    async with async_session() as session:
        yield session