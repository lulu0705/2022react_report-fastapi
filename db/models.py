from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    name = Column(String)
    location = Column(String)
    time = Column(String)
    store_avatar = Column(String)
    image = Column(String)
    price = Column(Integer)
    currency = Column(String)
    company = Column(String)
    hour = Column(String)
    MoreInfo = Column(String)
    buyer = relationship('DbReserve',back_populates='owner_product')
    disabledDate = relationship('DbDisabled',back_populates='owner_disabled')

class DbReserve(Base):
    __tablename__ = 'reserves'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    county = Column(String)
    addr = Column(String)
    area = Column(Integer)
    # time = Column(Integer,nullable=False)
    reserve_date = Column(DateTime)
    # product_id = Column(Integer)
    product_id = Column(Integer, ForeignKey('product.id'))
    owner_product = relationship('DbProduct',back_populates='buyer')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    typename = Column(String)
    name = Column(String)
    email = Column(String)
    comment = Column(String)


class DbNewpost(Base):
    __tablename__ = 'newpost'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    image = Column(String)
    release = Column(DateTime)
    # release = Column(String)


class DbDisabled(Base):
    __tablename__ = 'disabled'
    id = Column(Integer, primary_key=True, index=True)
    disabledDate_0 = Column(DateTime)
    disabledDate_1 = Column(DateTime)
    disabledDate_2 = Column(DateTime)
    user_id = Column(Integer, ForeignKey('product.id'))
    owner_disabled = relationship('DbProduct',back_populates='disabledDate')
