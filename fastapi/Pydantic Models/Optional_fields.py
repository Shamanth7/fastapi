from typing import Optional

class Product(BaseModel):
    name: str               # required
    price: float            # required
    in_stock: bool = True   # optional, defaults to True
    description: Optional[str] = None   # optional, can be null