import email
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Union
from app.database.schemas import Schemas
from ..config import get_session
from app.database.models import models
from fastapi import HTTPException
from app.crud import crud

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


# get User
@router.get("/", tags=["user"], response_model=List[Schemas.UsersView])
def getUsers(
    username: Union[str, None] = None,
    email: Union[str, None] = None,
    page: int = 1,
    per_page: int = 20,
    session: Session = Depends(get_session),
):
    getUser = crud.getUser(session, username, email, page, per_page)
    return getUser


@router.post("/", tags=["user"], response_model=Schemas.UsersView)
def Register(
    users: Schemas.UsersCreat,
    session: Session = Depends(get_session),
):
    register = crud.register(session, users)
    print(register)
    return register


@router.put("/{id}", tags=["user"])
def updateUsers(id: int, user: Schemas.Users, session: Session = Depends(get_session)):
    return crud.updateUser(session, id, user)


@router.delete("/{id}", tags=["user"])
def deleteUsers(id: int, session: Session = Depends(get_session)):
    found = session.query(models.Users).get(id)
    if not found:
        raise HTTPException(status_code=404, detail="Not found user")
    session.delete(found)
    session.commit()
    session.close()
    return "Delete Users succesfully!"
