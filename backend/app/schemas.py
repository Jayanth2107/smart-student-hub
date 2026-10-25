from datetime import date
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Jayanth MS"
    )

    email: EmailStr = Field(
        ...,
        example="jayanth@example.com"
    )

    password: str = Field(
        ...,
        min_length=8,
        example="Password@123"
    )

    gender: str = Field(
        ...,
        example="Male"
    )

    date_of_birth: date = Field(
        ...,
        example="2004-07-15"
    )

    role: str = Field(
        default="Student",
        example="Student"
    )


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    gender: str
    date_of_birth: date
    age: int
    role: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr = Field(
        ...,
        example="jayanth@example.com"
    )

    password: str = Field(
        ...,
        example="Password@123"
    )