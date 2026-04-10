from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str   = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)           # greater than 0
    quantity: int = Field(..., ge=1, le=1000) # 1 to 1000
    sku: str = Field(..., pattern=r"^[A-Z]{3}-\d{4}$")