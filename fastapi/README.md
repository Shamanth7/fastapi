**Key Things to Know**
```@app.get```, ```@app.post```, ```@app.put```, ```@app.delete```

 these decorators map HTTP methods to your functions.<br>
Type hints like item_id: int are not just style — FastAPI uses them to validate and convert data automatically.
HTTPException is how you return error responses with proper status codes.
<br>/docs — always visit this after starting your server. It's a live UI where you can test every endpoint.