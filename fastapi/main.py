from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory "database"
items = {}

class Item(BaseModel):
    name: str
    price: float

# CREATE
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

# READ
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    items.pop(item_id, None)
    return {"message": "deleted"}

