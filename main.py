from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Session
from db.db import engine 
from models.products_model import Products

app = FastAPI()

origins = ["*"]

session = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/gem")
def create_gem(product: Products):
    try:
        create_db_and_tables()
    except:
        pass
    g = product(product.name,
        product.descript,
        product.price,)
    session.add(g)
    session.commit()
    session.refresh(g)
    return g



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


