import email
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.database.schemas import userSchemas, memberSchemas
from ..config import get_session
from app.database.models import models
from fastapi import HTTPException

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

# get Al
@router.get("/", tags=["user"], response_model=List[userSchemas.Item])
def getAllUsers(session: Session = Depends(get_session)):
    items = session.query(models.Users).all()
    return items


# get 1 user


@router.get("/{id}", tags=["user"], response_model=List[userSchemas.Item])
def getOneItem(id: int, session: Session = Depends(get_session)):
    ittem = session.query(models.Users).get(id)
    try:
        return ittem
    finally:
        print(ValueError)


@router.post("/", tags=["user"], response_model=userSchemas.Item)
def postItem(
    item: userSchemas.Item,
    session: Session = Depends(get_session),
):
    items = models.Users(
        username=item.username, hash_Pwd=item.hash_Pwd, email=item.email, role=item.role
    )
    session.add(items)
    session.commit()
    session.refresh(items)
    return items


@router.put("/{id}", tags=["user"])
def updateItem(
    id: int, item: userSchemas.Item, session: Session = Depends(get_session)
):
    ittem = session.query(models.Users).get(id)
    if ittem == None:
        raise HTTPException(status_code=404, detail="not found")
    ittem.username = item.username
    item = models.Users(username=item.username)
    session.commit()
    return ittem


@router.delete("/{id}", tags=["user"])
def deleteItem(id: int, session: Session = Depends(get_session)):
    found = session.query(models.Users).get(id)
    if not found:
        raise HTTPException(status_code=404, detail="Not found user")
    session.delete(found)
    session.commit()
    session.close()
    return "Delete item succesfully!"


@router.post("/member", tags=["user"], response_model=memberSchemas.Member)
def postItem(
    item: memberSchemas.Member,
    session: Session = Depends(get_session),
):
    items = models.Member(
        username=item.username, hash_Pwd=item.hash_Pwd, email=item.email, role=item.role
    )
    session.add(items)
    session.commit()
    session.refresh(items)
    return items
