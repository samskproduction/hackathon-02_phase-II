from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class UserBase(SQLModel):
    email: str
    name: Optional[str] = None

from uuid import uuid4

class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)  # Auto-generate UUID
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    hashed_password: Optional[str] = Field(default=None)  # Store hashed password, optional for existing users
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    email: str
    password: str  # This would be hashed
    name: Optional[str] = None

class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None

class UserResponse(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime