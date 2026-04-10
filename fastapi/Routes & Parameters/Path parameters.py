@app.get("/users/{user_id}")
def get_user(user_id: int):   # FastAPI auto-converts to int
    return {"id": user_id}
# Call: GET /users/42