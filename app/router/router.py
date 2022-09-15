from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app.database.schemas import userSchemas
from ..config import get_session
from app.database.models import models

router = APIRouter(
        prefix='/user',
        tags=['user'],
        )

@router.get('/', tags=['user'], response_model=List[userSchemas.Item])
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Users).all()
    return items
