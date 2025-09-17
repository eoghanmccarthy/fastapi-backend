# Pydantic models define the structure of data coming in and going out of your API
# These are different from SQLAlchemy models (which define database tables)
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# Base schema with common fields
# Other schemas will inherit from this
class UserBase(BaseModel):
    # Name is required
    name: str
    # Use EmailStr for automatic email validation
    email: EmailStr  # This validates email format automatically

# Schema for creating a user (incoming data from API request)
# This defines what fields the client must send when creating a user
class UserCreate(UserBase):
    # Inherits name and email from UserBase
    # Could add password or other create-specific fields here
    pass

# Schema for updating a user (incoming data for updates)
# All fields are optional since user might only want to update some fields
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

# Schema for returning user data (outgoing data from API response)
# This includes all the database fields including auto-generated ones
class User(UserBase):
    # Include the database-generated fields
    id: int
    is_active: bool
    created_at: datetime

    # This tells Pydantic to work with SQLAlchemy models
    # It allows Pydantic to read data from SQLAlchemy objects
    class Config:
        from_attributes = True

# Schema for user lists (when returning multiple users)
# This is the same as User but makes the API documentation clearer
class UserResponse(User):
    pass

# Base schema for posts
class PostBase(BaseModel):
    title: str
    content: str

# Schema for creating a post
class PostCreate(PostBase):
    # owner_id will be set from the URL parameter, not the request body
    pass

# Schema for updating a post
class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

# Schema for returning post data
class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
