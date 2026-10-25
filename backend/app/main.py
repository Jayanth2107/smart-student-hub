from datetime import date

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, get_db
from . import models, schemas
from .auth import hash_password

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Student Hub API")


@app.get("/")
def home():
    return {"message": "Smart Student Hub Backend Running"}


def calculate_age(date_of_birth: date):
    today = date.today()

    age = (
        today.year
        - date_of_birth.year
        - (
            (today.month, today.day)
            < (date_of_birth.month, date_of_birth.day)
        )
    )

    return age


@app.post("/register", response_model=schemas.UserResponse)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    # Check duplicate email
    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email.lower())
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    # Future DOB validation
    if user.date_of_birth > date.today():
        raise HTTPException(
            status_code=400,
            detail="Date of birth cannot be in the future."
        )

    # Calculate age
    age = calculate_age(user.date_of_birth)

    # Minimum age validation
    if age < 5:
        raise HTTPException(
            status_code=400,
            detail="Student must be at least 5 years old."
        )

    # Create new user
    new_user = models.User(
        full_name=user.full_name.strip(),
        email=user.email.lower(),
        password=hash_password(user.password),
        gender=user.gender,
        date_of_birth=user.date_of_birth,
        age=age,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user