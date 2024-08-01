from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(prefix="/users", tags=["User"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    """Create new user"""
    try:
        user.hashed_password = utils.create_hash(user.hashed_password)
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User with email already exist!")

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    """Retrieve a specific user"""
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"user with id {id} does not exist!")
    return user
