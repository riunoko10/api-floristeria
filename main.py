from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


all_products = [
    {
        "id": 1,
        "name": "Producto 1",
        "price": 100,
        "descript": "Descripcion del producto 1"
    },
{
        "id": 12,
        "name": "Producto 2",
        "price": 200,
        "descript": "Descripcion del producto 2"
    },
{
        "id": 3,
        "name": "Producto 3",
        "price": 300,
        "descript": "Descripcion del producto 3"
    },
]

@app.get("/items")
def read_item():
    return all_products





app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


