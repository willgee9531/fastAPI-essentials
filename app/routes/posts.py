from fastapi import APIRouter, status, HTTPException, Depends
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Annotated
from ..oauth2 import get_current_user


router = APIRouter(prefix="/posts", tags=["Post"])


@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    """Retrieve all posts"""
    # cursor.execute(""" SELECT * FROM posts """)
    # posts = cursor.fetchall()

    posts = db.query(models.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    """Create a post"""
    new_posts = models.Post(**post.model_dump())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts

@router.get("/{id}", response_model=schemas.Post)
def create_posts(id: int, db: Session = Depends(get_db)):
    """Retrieve a single post"""
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found!")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    """Delete a single post"""
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post does not exist!")
    post.delete(synchronize_session=False)
    db.commit()
    return {"message": "post successfully deleted"}

@router.put("/{id}", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def update_post(id: int, post_update: schemas.PostCreate, db: Session = Depends(get_db)):
    """Update/edit a post"""
    post = db.query(models.Post).filter(models.Post.id == id)
    first_post = post.first()
    if not first_post:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post does not exist!")
    post.update(post_update.model_dump(), synchronize_session=False)
    db.commit()
    return post.first()