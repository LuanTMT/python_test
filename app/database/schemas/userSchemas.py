from pydantic import BaseModel
from typing import List, Literal, Optional, Union


class Item(BaseModel):
    username: Union[str, None] = None
    hash_Pwd: Union[str, None] = None
    email: Union[str, None] = None
    role: Union[str, None] = None

    class Config:
        orm_mode = True
