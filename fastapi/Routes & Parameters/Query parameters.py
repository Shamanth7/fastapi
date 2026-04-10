@app.get("/search")
def search(
    keyword: str,          # required — no default
    page: int = 1,         # optional — has default
    limit: int = 20        # optional — has default
):
    return {"keyword": keyword, "page": page}
# Call: GET /search?keyword=python&page=2
