from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

# Create database tables when the app starts
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Backend", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is running!"}


@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    # Step 1: Create a Python object of class User
    # This creates an instance but doesn't save it to database yet
    # SQLAlchemy knows this will go to the 'users' table because
    # the User class has __tablename__ = "users"
    user = models.User(name=name, email=email)

    # Step 2: Add the user object to the database session
    # This stages the object for insertion but doesn't save it yet
    # SQLAlchemy looks at the object type (User) and knows to use the 'users' table
    db.add(user)

    # Step 3: Actually save the changes to the database
    # This executes the INSERT SQL statement
    # Without commit(), the user won't be saved
    db.commit()

    # Step 4: Refresh the object to get the database-generated values
    # This updates our 'user' object with the ID and created_at timestamp
    # that the database automatically generated
    db.refresh(user)

    # Step 5: Return the complete user object (now with ID and timestamps)
    return user


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
