from fastapi import HTTPException, Depends, APIRouter, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import schemas, models, utils, oauth2
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post("/login", tags=["Auth"], status_code=status.HTTP_200_OK)
def login(user_details: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_details.username).first()

    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect email or password")
    
    if not utils.verify_hash(user_details.password, user.hashed_password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}

