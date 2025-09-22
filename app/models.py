# MODELS MODULE NOTE
# This module (app/models.py) defines the SQLAlchemy ORM models that map your
# Python classes to database tables. Each class below represents a table, and
# each class attribute of type Column(...) represents a table column.
#
# Key ideas:
# - Base inheritance: All models inherit from Base (declared in app/database.py).
#   SQLAlchemy uses this to collect table metadata (names, columns, constraints)
#   so it can create tables (e.g., via Base.metadata.create_all) or generate
#   migrations when using Alembic.
# - Not Pydantic: These are database models (ORM) — different from the Pydantic
#   schemas in app/schemas.py which shape request/response payloads. Routes use
#   Pydantic for validation/serialization and use these ORM models for database IO.
# - Relationships: The User ↔ Post relationship is modeled with ForeignKey and
#   relationship(..., back_populates=...), allowing convenient navigation like
#   user.posts and post.owner while keeping referential integrity in the DB.
# - Migrations: In development you can rely on Base.metadata.create_all(...) to
#   bootstrap tables, but in production prefer Alembic migrations to apply
#   versioned, auditable schema changes safely (see notes in app/main.py).
# - Extending the data model: To add new tables/columns, define a new class or
#   column here, then create and apply a migration (alembic revision --autogenerate
#   && alembic upgrade head) so the physical database schema matches these models.

# Import the column types we need to define our database table structure
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

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

    # ADD THIS LINE - Define relationship to posts
    # This creates a "virtual" field that lets you access user.posts
    # back_populates="owner" connects to the owner field in Post model
    posts = relationship("Post", back_populates="owner")


# Define our Post table as a Python class
# This class represents a table in our database - shows relationship with User
class Post(Base):
    # Tell SQLAlchemy what the actual table name should be in the database
    __tablename__ = "posts"

    # Primary key for posts
    id = Column(Integer, primary_key=True, index=True)

    # Post title
    title = Column(String, index=True)

    # Post content - Text allows longer content than String
    content = Column(Text)

    # Foreign key - this links each post to a user
    # ForeignKey("users.id") means this column references the id column in users table
    # When you create a post, you must specify which user owns it
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Timestamp when post was created
    created_at = Column(DateTime, server_default=func.now())

    # Define relationship to user
    # This creates a "virtual" field that lets you access post.owner
    # back_populates="posts" connects to the posts field in User model
    owner = relationship("User", back_populates="posts")


# The relationships create these connections:
# - user.posts → gives you all posts by that user
# - post.owner → gives you the user who created that post
# - This is a "one-to-many" relationship (one user, many posts)
