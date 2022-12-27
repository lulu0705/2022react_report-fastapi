from pydantic import BaseModel
from typing import List
from datetime import datetime

class ProductRequestSchema(BaseModel):
    category: str
    name: str
    location: str
    time: str
    store_avatar: str
    image: str
    price: int
    currency: str
    company: str
    hour: str
    MoreInfo: str


class ProductResponseSchema(ProductRequestSchema):
    id: int

    class Config:
        orm_mode = True


class ProductResponseWith(ProductRequestSchema):
    id: int

    class Config:
        orm_mode = True


# -------------------------------------------
class ReserveRequestSchema(BaseModel):
    name: str
    phone: str
    email: str
    county: str
    addr: str
    area: str
    # time: str
    reserve_date: datetime
    product_id: str


class ReserveResponseSchema(ReserveRequestSchema):
    id: int
    product_id: int
    # clicked_likes: CardResponseSchema

    class Config:
        orm_mode = True


class ReserveResponseWithProductSchema(ReserveRequestSchema):
    id: int
    product_id: int
    owner_product: ProductResponseSchema

    class Config:
        orm_mode = True


# -------------------------------------------
class CommentRequestSchema(BaseModel):
    typename: str
    name: str
    email: str
    comment: str


class CommentResponseSchema(CommentRequestSchema):
    id: int

    class Config:
        orm_mode = True


# -------------------------------------------
class NewpostRequestSchema(BaseModel):
    title: str
    description: str
    image: str
    release: datetime


class NewpostResponseSchema(NewpostRequestSchema):
    id: int

    class Config:
        orm_mode = True

# -------------------------------------------
class DisabledRequestSchema(BaseModel):
    disabledDate_0: datetime
    disabledDate_1: datetime
    disabledDate_2: datetime
    user_id: int


class DisabledResponseSchema(DisabledRequestSchema):
    id: int

    class Config:
        orm_mode = True


class ProductResponseWithReserveSchema(ProductRequestSchema):
    id: int
    buyer: List[ReserveResponseSchema] = []
    disabledDate: List[DisabledResponseSchema] = []

    class Config:
        orm_mode = True


# class ProductResponseWithDisabledSchema(ProductRequestSchema):
#     id: int
#     disabledDate: List[DisabledResponseSchema] = []

#     class Config:
#         orm_mode = True
