from fastapi import APIRouter
from app.router import router

rout = APIRouter( prefix='/v1', tags=['v1'],)

rout.include_router(router.router)