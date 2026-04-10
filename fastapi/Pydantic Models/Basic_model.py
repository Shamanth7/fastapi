from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    # user.name, user.email, user.age are all available
    return {"created": user.name}