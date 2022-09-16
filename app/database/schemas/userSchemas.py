from pydantic import BaseModel


class Item(BaseModel):
    username: str
    hash_Pwd: str
    email: str
    role: str
