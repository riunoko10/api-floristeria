from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from enum import Enum as Enum_, IntEnum



class Products(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float
    name: str
    descript: str