from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(50), nullable=False)

    email = Column(String(100), unique=True, index=True, nullable=False)

    password = Column(String, nullable=False)

    gender = Column(String(10), nullable=False)

    date_of_birth = Column(Date, nullable=False)

    age = Column(Integer, nullable=False)

    role = Column(String(20), default="Student")

    created_at = Column(DateTime, default=datetime.utcnow)