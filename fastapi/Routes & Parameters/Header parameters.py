from fastapi import Header

@app.get("/protected")
def protected_route(x_token: str = Header(...)):  # ... means required
    return {"token": x_token}
# Call: GET /protected  (with header X-Token: abc)