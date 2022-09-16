from fastapi import FastAPI, Body, Depends
from app.database.schemas import userSchemas
from app.database.models import models
from app.router import rout
from .config import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


app = FastAPI()

# get All

app.include_router(rout)


@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Users).all()
    return items


# get 1 item


@app.get("/{id}")
def getOneItem(id: int, session: Session = Depends(get_session)):
    ittem = session.query(models.Users).get(id)
    return ittem


@app.post("/")
def postItem(item: userSchemas.Item, session: Session = Depends(get_session)):
    items = models.Users(username=item.username)
    session.add(items)
    session.commit()
    session.refresh(items)
    return items


@app.put("/{id}")
def updateItem(
    id: int, item: userSchemas.Item, session: Session = Depends(get_session)
):
    ittem = session.query(models.Item).get(id)
    ittem.task = item.task
    item = models.Item(task=item.task)
    session.commit()
    return ittem


@app.delete("/{id}")
def deleteItem(id: int, session: Session = Depends(get_session)):
    session.delete(session.query(models.Item).get(id))
    session.commit()
    session.close()
    return "Delete item succesfully!"
