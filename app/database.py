# Import the function that creates a connection to your database
# Think of this as importing the "database connector" tool
from sqlalchemy import create_engine

# Import a tool that lets you define database tables using Python classes
# Instead of writing raw SQL like CREATE TABLE users..., you'll write Python classes
from sqlalchemy.ext.declarative import declarative_base

# Import a tool that creates "sessions" - these are like conversations with your database
# Each session handles a group of database operations
from sqlalchemy.orm import sessionmaker

# This is the "address" of your database
# sqlite:// = "Use SQLite database"
# ./app.db = "Create/use a file called 'app.db' in the current folder"
# The file doesn't exist yet - SQLAlchemy will create it when needed
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Create the actual connection to your database
# SQLALCHEMY_DATABASE_URL = Uses the SQLite file we defined above
# check_same_thread": False = This is SQLite-specific. Normally SQLite only allows
# one thread to access it, but FastAPI uses multiple threads, so we disable this restriction
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a "session factory" - a template for creating database conversations
# autocommit=False = Don't automatically save changes (you'll control when to save with commit())
# autoflush=False = Don't automatically send changes to database until you're ready
# bind=engine = Connect this session maker to our database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class that all your database models (tables) will inherit from
# When you create a User or Item class later, they'll extend this Base
Base = declarative_base()


# This is a "dependency" function for FastAPI
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Give this session to whoever needs it (your API endpoints)
        yield db
    finally:
        # Always close the session when done, even if an error happens
        db.close()
