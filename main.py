from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from database_models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

database_models.Base.metadata.create_all(bind=engine)

Products = [
    Product(id = 1, name = "phone", description = "budget phone", price = 9999, quantity=10),
    Product(id = 2, name = "laptop", description = "ASUS laptop", price = 60000, quantity=5),
    Product(id = 3, name = "pen drive", description = "SSD with 64GB storage", price = 499, quantity=15),
    Product(id = 4, name = "mouse", description = "Gaming mouse", price = 399, quantity=20),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in Products:
            db.add(product)
        db.commit()

init_db()


@app.get("/products/")
def get_all(db : Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_by_id(id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"

@app.post("/products/")
def add_product(product:models.Product, db : Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
    
@app.put("/products/{id}")
def update_by_id(id:int, product:models.Product, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "Product Not Found"


@app.delete("/products/{id}")
def delete(id:int, db : Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Deleted Successfully"
    else:
        return "Product not found"
    