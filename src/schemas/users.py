from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Sign up request schema."""
    email: EmailStr
    user_name: str
    password: str


class UserBase(BaseModel):
    """Response schema with user details."""
    id: int
    email: EmailStr
    user_name: str
