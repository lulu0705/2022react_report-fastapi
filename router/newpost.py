from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import NewpostRequestSchema, NewpostResponseSchema

from db.database import get_db
from db import db_newpost
from typing import List

router = APIRouter(
    prefix='/api/v1/newpost',
    tags=['newpost']
)


@router.post('', response_model=NewpostResponseSchema)
def create(request: NewpostRequestSchema, db: Session = Depends(get_db)):
    return db_newpost.create(db=db, request=request)


@router.get('/all', response_model=List[NewpostResponseSchema])
def get_all_newposts(db: Session = Depends(get_db)):
    return db_newpost.get_all_newposts(db)


@router.get("/all/topthree", response_model=List[NewpostResponseSchema])
def get_newpost_topthree(db: Session = Depends(get_db)):
    return db_newpost.get_newpost_topthree(db=db)