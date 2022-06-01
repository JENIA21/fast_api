from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Sign up request schema."""
    email: EmailStr
    name: str
    password: str


class UserBase(BaseModel):
    """Response schema with user details."""
    email: EmailStr
    name: str
    password: str
