from fastapi import HTTPException, status
from router.schemas import ReserveRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbReserve


def create(db: Session, request: ReserveRequestSchema) :
    new_reserve = DbReserve(
        name=request.name,
        phone=request.phone,
        email=request.email,
        county=request.county,
        addr=request.addr,
        area=request.area,
        # time=request.time,
        reserve_date=request.reserve_date,
        product_id=request.product_id,

    )
    db.add(new_reserve)
    db.commit()
    db.refresh(new_reserve)
    return new_reserve
    # try:
    #     db.add(new_reserve)
    #     db.commit()
    #     db.refresh(new_reserve)
    #     access_token = create_access_token(data={'username': new_reserve.username})
    #     return {
    #         'access_token': access_token,
    #         'user_id': new_user.id,
    #         'username': new_user.username,
    #         'tel': '',
    #         'address': ''
    #     }
    # except IntegrityError as exc:
        # db.rollback()
        # raise HTTPException(status_code=400, detail=f"{exc}".split('\n')[0])


def get_all_reserves(db: Session):
    reserves = db.query(DbReserve).all()
    if not reserves:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reserves not found')
    return reserves


def get_reserve_by_id(reserve_id: int, db: Session):
    reserve = db.query(DbReserve).filter(DbReserve.id == reserve_id).first()
    if not reserve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Reserve with id = {reserve_id} not found')
    return reserve


    user = db.query(DbUser).filter(func.upper(DbUser.username) == user_name.upper()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with user name = {user_name} not found')
    return user