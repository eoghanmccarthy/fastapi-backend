# Import the column types we need to define our database table structure
from sqlalchemy import Column, Integer, String, DateTime, Boolean

# Import func to use database functions like getting the current timestamp
from sqlalchemy.sql import func

# Import the Base class we created in database.py
# All our database models (tables) will inherit from this Base
from .database import Base


# Define our User table as a Python class
# This class represents a table in our database
class User(Base):
    # Tell SQLAlchemy what the actual table name should be in the database
    __tablename__ = "users"

    # Define the 'id' column:
    # Integer = column stores whole numbers
    # primary_key=True = this is the unique identifier for each row
    # index=True = create an index on this column for faster lookups
    id = Column(Integer, primary_key=True, index=True)

    # Define the 'name' column:
    # String = column stores text
    # index=True = create an index for faster searching by name
    name = Column(String, index=True)

    # Define the 'email' column:
    # String = column stores text
    # index=True = create an index for faster searching by email
    email = Column(String, unique=True, index=True)

    # Define the 'is_active' column:
    # Boolean = column stores True/False values
    # default=True = new users are active by default
    is_active = Column(Boolean, default=True)

    # Define the 'created_at' column:
    # DateTime = column stores date and time
    # server_default=func.now() = automatically set to current time when row is created
    # func.now() tells the database to use its built-in "get current time" function
    created_at = Column(DateTime, server_default=func.now())

# When this model is used, it will create a table that looks like:
#
# users table:
# ┌────┬────────────┬──────────────────┬───────────┬─────────────────────┐
# │ id │    name    │      email       │ is_active │     created_at      │
# ├────┼────────────┼──────────────────┼───────────┼─────────────────────┤
# │ 1  │ "John Doe" │ "john@email.com" │    True   │ 2024-01-15 10:30:00 │
# │ 2  │ "Jane Doe" │ "jane@email.com" │    True   │ 2024-01-15 11:45:00 │
# └────┴────────────┴──────────────────┴───────────┴─────────────────────┘