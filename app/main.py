from fastapi import FastAPI
from app.router import rout
from .config import Base, engine


Base.metadata.create_all(engine)

app = FastAPI()

# get All

app.include_router(rout)
