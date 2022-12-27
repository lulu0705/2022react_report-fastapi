from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import ReserveRequestSchema, ReserveResponseSchema, ReserveResponseWithProductSchema

from db.database import get_db
from db import db_reserve
from typing import List

router = APIRouter(
    prefix='/api/v1/reserve',
    tags=['reserve']
)


@router.post('', response_model=ReserveResponseSchema)
def create(request: ReserveRequestSchema, db: Session = Depends(get_db)):
    return db_reserve.create(db=db, request=request)


@router.get('/all', response_model=List[ReserveResponseSchema])
def get_all_reserves(db: Session = Depends(get_db)):
    return db_reserve.get_all_reserves(db)



@router.get('/id/{reserve_id}', response_model=ReserveResponseWithProductSchema)
def get_reserve_by_id(reserve_id: int, db: Session = Depends(get_db)):
    return db_reserve.get_reserve_by_id(reserve_id=reserve_id, db=db)
