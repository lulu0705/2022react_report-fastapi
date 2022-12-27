from fastapi import HTTPException, status
from router.schemas import CommentRequestSchema
from sqlalchemy.orm.session import Session
from sqlalchemy import func, exc
from sqlalchemy.exc import IntegrityError

from db.models import DbComment


def create(db: Session, request: CommentRequestSchema) :
    new_comment = DbComment(
        typename=request.typename,
        name=request.name,
        email=request.email,
        comment=request.comment,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
    

def get_all_comments(db: Session):
    comments = db.query(DbComment).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Comments not found')
    return comments

