from pydantic import BaseModel

class ProductStock(BaseModel):
    product_id: str
    bar_code: str
    overall_stock: int
    store_stock: int
    warehouse_stock: int
    last_updated: str
    is_active: bool