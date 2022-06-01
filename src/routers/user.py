from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas import users
from src.utils import users as users_utils
from src.utils.dependcies import get_current_user

router = APIRouter()


@router.post('/sign-up', response_model=users.UserBase)
async def create_user(user: users.UserCreate):
    db_user = await users_utils.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered.')
    return await users_utils.create_user(user=user)


@router.post('/auth', response_model=users.UserBase)
async def auth(format_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_utils.get_user_by_email(email=format_data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong e-mail or password')
    if not users_utils.validate_password(password=format_data.password, hashed_password=user['password']):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong e-mail or password')
    return await users_utils.create_user()


@router.get('/users/me', response_model=users.UserBase)
async def read_user(current_user: users.UserBase = Depends(get_current_user)):
    return current_user
