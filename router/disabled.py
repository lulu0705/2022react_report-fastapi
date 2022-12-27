from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import DisabledRequestSchema, DisabledResponseSchema

from db.database import get_db
from db import db_disabled
from typing import List

router = APIRouter(
    prefix='/api/v1/disabled',
    tags=['disabled']
)


@router.post('', response_model=DisabledResponseSchema)
def create(request: DisabledRequestSchema, db: Session = Depends(get_db)):
    return db_disabled.create(db=db, request=request)


@router.get('/all', response_model=List[DisabledResponseSchema])
def get_all_disableds(db: Session = Depends(get_db)):
    return db_disabled.get_all_disableds(db)

