from pydantic import BaseModel

class ProductInfo(BaseModel):
    id: str
    name: str
    price: float
    description: str
    category: str
    brand: str 
    weight: float
    unit: str
    is_active: bool

