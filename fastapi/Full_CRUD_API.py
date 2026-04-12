from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# --- Pydantic model ---
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# --- In-memory database (a plain dict) ---
db: dict[int, Product] = {
    1: Product(id=1, name="Wireless Mouse", price=799, in_stock=True),
    2: Product(id=2, name="USB-C Hub",      price=1499, in_stock=True),
}

# --- CREATE ---
@app.post("/products", status_code=201)
def create_product(product: Product):
    if product.id in db:
        raise HTTPException(status_code=400, detail="ID already exists")
    db[product.id] = product
    return product

# --- READ one ---
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    return db[product_id]

# --- READ all ---
@app.get("/products")
def list_products():
    return list(db.values())

# --- UPDATE ---
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    db[product_id] = product
    return product

# --- DELETE ---
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    del db[product_id]
    return {"message": "Product deleted"}