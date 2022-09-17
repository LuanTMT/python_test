from typing import Union, List
from sqlalchemy.orm import Session
from app.database.models import models
from fastapi import HTTPException
from sqlalchemy.orm import Query
from fastapi import Query as FastapiQuery
from app.crud.service import service


def build_user_query(
    session: Session, username: Union[str, None], email: Union[str, None] = None
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
