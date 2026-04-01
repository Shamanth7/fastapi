from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, name: str = "unknown"):
    return {"item_id": item_id, "name": name}

# Path parameter — part of the URL
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Query parameter — comes after ?
@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}
    # Call: /search?keyword=python&limit=5

@app.get("/posts/{post_id}/comments")
def get_comments(post_id: int, limit: int = 5):
    return {"post_id": post_id, "limit": limit}

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True   # default value

@app.post("/items/")
def create_item(item: Item):
    return {"received": item.name, "price": item.price}