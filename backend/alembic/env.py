import asyncio
# from logging.config import fileConfig
from sqlalchemy import pool
# from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine#, AsyncEngine
from alembic import context
from dotenv import load_dotenv
import os
import sys

# Load the .env file
load_dotenv()

# Load the database URL from the .env file
DATABASE_URL = os.getenv("DATABASE_URL_ALEMBIC")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL_ALEMBIC is not set. Please check your .env file.")

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.auth.models import User  # noqa: E402, F401
from src.delivery_locations.models import DeliveryLocation  # noqa: E402, F401
from src.products.models import Product  # noqa: E402, F401
from src.deliveries.models import Delivery # noqa: E402, F401
from src.database import Base  # noqa: E402

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.configure

# # Interpret the config file for Python logging.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# Import your Base object
target_metadata = Base.metadata


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    
    # Create the AsyncEngine
    connectable = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
        future=True
    )

    def do_run_migrations(connection):
        # This is now a synchronous function
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

    async def run_with_connection():
        async with connectable.connect() as connection:
            await connection.run_sync(do_run_migrations)

    asyncio.run(run_with_connection())

run_migrations_online()
