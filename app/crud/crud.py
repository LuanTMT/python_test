from re import S
from typing import Union, List
from sqlalchemy.orm import Session
from app.database.models import models
from fastapi import HTTPException
from sqlalchemy.orm import Query
from fastapi import Query as FastapiQuery
from app.crud.service import service
import hashlib
from app.database.schemas import Schemas


def build_user_query(
    session: Session, username: Union[str, None], email: Union[str, None]
) -> Query:
    query = session.query(models.Users)

    if username:
        query = query.filter(models.Users.username == username)
    if email:
        query = query.filter(models.Users.email == email)
    # query = query.order_by(models.Users.id.desc())

    return query


def getUser(
    session: Session,
    username: Union[str, None] = None,
    email: Union[str, None] = None,
    page: int = 1,
    per_page: int = 20,
) -> List[models.Users]:
    per_page = service.validate_page(parameters=per_page)
    page = service.validate_page(parameters=page, page=True)
    query = build_user_query(session=session, username=username, email=email)
    query = query.offset((page - 1) * per_page).limit(per_page)
    users = query.all()
    return users

def getUserbyId(session:Session, id :int):
    return session.query(models.Users).get(id)


def getUserbyUsername(session: Session, username: str):
    return session.query(models.Users).filter(models.Users.username == username).first()


def getUserbyEmail(session:Session, email: str):
    return session.query(models.Users).filter(models.Users.email == email).first()


def register(session: Session, user: Schemas.UsersCreat):
    findUsername = getUserbyUsername(session, user.username)
    findEmail = getUserbyEmail(session, user.email)
    if findUsername:
        raise HTTPException(
            status_code=404, detail=f"Username: {findUsername.username} đã tồn tại "
        )
    if findEmail:
        raise HTTPException(status_code=404, detail=f"Email: {findEmail.email} đã tồn tại ")

    # ma hoa pwd
    hash_object = hashlib.sha384(user.password.encode())
    hex_dig = hash_object.hexdigest()
    # Users = models.Users(**user.dict())
    user = models.Users(
        username=user.username, hash_Pwd=hex_dig, email=user.email, role=user.role
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def updateUser(session: Session, id:int, userUpdate = Schemas.UsersUpdate ):
    user = getUserbyId(session, id)
    if user is not None:
        user.username = userUpdate.username
        Users = models.Users(username=user.username)
        session.commit()   
        return Users
    else:
        raise HTTPException(status_code=404, detail="Users Not Found")


