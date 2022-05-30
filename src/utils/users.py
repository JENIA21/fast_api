"""Different helper-functions to work with users."""
import hashlib
import random
import string
from datetime import datetime, timedelta
from sqlalchemy import and_

from src.db import database
from src.user_models import users_table
from src.schemas import users as user_schema


def get_random_string(length=12):
    """Return generated random string (salt)."""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(password: str, salt: str = None):
    """Hash password with salt."""
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
    return enc.hex()


def validate_password(password: str, hashed_password: str):
    """Validate password hash with db hash."""
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed


async def get_user_by_email(email: str):
    """Return user info by email."""
    query = users_table.select().where(users_table.c.email == email)
    return await database.fetch_one(query)


async def create_user(user: user_schema.UserCreate):
    """Create new user."""
    salt = get_random_string()
    hashed_password = hash_password(user.password, salt)
    query = users_table.insert().values(
        email=user.email, name=user.name, password=f"{salt}${hashed_password}"
    )
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}
