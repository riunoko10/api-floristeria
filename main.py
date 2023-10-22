from typing import Union
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import config as cfg

app = FastAPI()

origins = ["*"]



class Product(BaseModel):
    name:str
    price:int
    category: str
    descript: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/products")
def read_item():
    return cfg.all_products


@app.post("/product")
def add_product(product: Product):
    product = jsonable_encoder(product)
    product["id"] = len(cfg.all_products) + 1
    product = Product(**product)
    cfg.all_products.append(product)
    return cfg.all_products


@app.get("/product/{id}")
def get_product(id: int):
    products = cfg.all_products
    product_response = None
    for product in products:
        if product["id"] == id:
            product_response = product
    
    if product_response:
        return product_response
    else:
        return {"message": "Producto no encontrado"}





app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


