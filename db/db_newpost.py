from fastapi import HTTPException, status
from router.schemas import NewpostRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbNewpost


def create(db: Session, request: NewpostRequestSchema) :
    new_newpost = DbNewpost(
        title=request.title,
        description=request.description,
        image=request.image,
        release=request.release,
    )
    db.add(new_newpost)
    db.commit()
    db.refresh(new_newpost)
    return new_newpost
    

def get_all_newposts(db: Session):
    newposts = db.query(DbNewpost).all()
    if not newposts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Newposts not found')
    return newposts


def get_newpost_by_id( db: Session):
    newpost = db.query(DbNewpost).filter(DbNewpost.id).first()
    if not newpost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Newpost with not found')
    return newpost

# .filter(DbNewpost.id).limit(3).all()
def get_newpost_topthree(db: Session):
    newpost = db.query(DbNewpost).order_by(DbNewpost.id.desc()).limit(3).all()
    if not newpost:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Topthree Newpost with not found')
    return newpost