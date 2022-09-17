from sqlalchemy import (
    ForeignKey,
    Column,
    Integer,
    String,
    VARCHAR,
    Text,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship
from ...config import Base


# One Users to many Carts
class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    email = Column(Text, nullable=False)
    hash_Pwd = Column(String(30))
    role = Column(String(30))
    created_at_user = Column(DateTime, nullable=False, server_default=func.now())
    type = Column(VARCHAR(40), nullable=False, server_default="default")
    userCarts = relationship("Carts", backref="Users")
    userOrder = relationship("Orders", backref="Users")


class Products(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    price = Column(Integer)
    productCarts = relationship("Carts", backref="Products")
    orDetailCarts = relationship("OrderDetails", backref="Products")


class Orders(Base):
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    price = Column(Integer)
    user_id = Column(Integer, ForeignKey("Users.id"))
    order = relationship("OrderDetails", backref="Orders")


class OrderDetails(Base):
    __tablename__ = "OrderDetails"
    id = Column(Integer, primary_key=True)
    quanlityProduct = Column(Integer)
    order_id = Column(Integer, ForeignKey("Orders.id"))
    product_id = Column(Integer, ForeignKey("Products.id"))


class Carts(Base):
    __tablename__ = "Carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    product_id = Column(Integer, ForeignKey("Products.id"))
