from datetime import datetime
from pydantic import BaseModel
from typing import List, Literal, Optional, Union


class Users(BaseModel):
    username: Union[str, None] = None
    email: Union[str, None] = None
    role: Union[str, None] = None

    class Config:
        orm_mode = True


class UsersCreat(Users):
    password: Union[str, None] = None


class UsersUpdate(Users):
    pass


class UsersView(Users):
    id: int
    hash_Pwd: Optional[str]
    created_at_Users: Union[datetime, None] = None


class Products(BaseModel):
    title: str
    price: str

    class Config:
        orm_mode = True


class Orders(BaseModel):
    title: str
    price: str
    user_id: int

    class Config:
        orm_mode = True


class OrderDetails(BaseModel):
    quanlityProduct: int
    order_id: int
    product_id: int

    class Config:
        orm_mode = True


class Carts(BaseModel):
    user_id: int
    product_id: int

    class Config:
        orm_mode = True
