from fastapi import HTTPException, status
from router.schemas import DisabledRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbDisabled

def create(db: Session, request: DisabledRequestSchema) :
    new_disabled = DbDisabled(
        disabledDate_0=request.disabledDate_0,
        disabledDate_1=request.disabledDate_1,
        disabledDate_2=request.disabledDate_2,
        user_id=request.user_id,
    )
    db.add(new_disabled)
    db.commit()
    db.refresh(new_disabled)
    return new_disabled
    

def get_all_disableds(db: Session):
    disableds = db.query(DbDisabled).all()
    if not disableds:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Disableds not found')
    return disableds

