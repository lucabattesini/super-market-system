from typing import Literal
from pydantic import BaseModel

class ProductStock(BaseModel):
    id: str
    bar_code: str
    overall_stock: int
    store_stock: int
    warehouse_stock: int
    last_updated: str

class ProductStockOperation(BaseModel):
    id: str
    data: int
    operation: Literal["add", "sub"]