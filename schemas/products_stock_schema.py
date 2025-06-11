from pydantic import BaseModel

class ProductStock(BaseModel):
    bar_code: str
    product_id: str
    overall_stock: int
    store_stock: int
    warehouse_stock: int