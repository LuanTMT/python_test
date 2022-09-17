import email
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Union
from app.database.schemas import Schemas
from ..config import get_session
from app.database.models import models
from fastapi import HTTPException
from app.crud import crud

# ma hoa pwd
import hashlib

hash_object = hashlib.sha384(b"Hello World")
hex_dig = hash_object.hexdigest()
print(hex_dig)

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


# get User
@router.get("/", tags=["user"], response_model=List[Schemas.Users])
def getUsers(
    username: Union[str, None] = None,
    email: Union[str, None] = None,
    page: int = 1,
    per_page: int = 20,
    session: Session = Depends(get_session),
):
    getUser = crud.getUser(session, username, email, page, per_page)
    return getUser


@router.post("/", tags=["user"], response_model=Schemas.Users)
def postUsers(
    Users: Schemas.Users,
    session: Session = Depends(get_session),
):
    Users = models.Users(
        username=Users.username,
        hash_Pwd=Users.hash_Pwd,
        email=Users.email,
        role=Users.role,
    )
    session.add(Users)
    session.commit()
    session.refresh(Users)
    return Users


@router.put("/{id}", tags=["user"])
def updateUsers(id: int, Users: Schemas.Users, session: Session = Depends(get_session)):
    ittem = session.query(models.Users).get(id)
    if ittem == None:
        raise HTTPException(status_code=404, detail="not found")
    ittem.username = Users.username
    Users = models.Users(username=Users.username)
    session.commit()
    return ittem


@router.delete("/{id}", tags=["user"])
def deleteUsers(id: int, session: Session = Depends(get_session)):
    found = session.query(models.Users).get(id)
    if not found:
        raise HTTPException(status_code=404, detail="Not found user")
    session.delete(found)
    session.commit()
    session.close()
    return "Delete Users succesfully!"


# @router.post("/member", tags=["user"], response_model=memberSchemas.Member)
# def postUsers(
#     Users: memberSchemas.Member,
#     session: Session = Depends(get_session),
# ):
#     Users = models.Member(
#         username=Users.username,
#         hash_Pwd=Users.hash_Pwd,
#         email=Users.email,
#         role=Users.role,
#     )
#     session.add(Users)
#     session.commit()
#     session.refresh(Users)
#     return Users
