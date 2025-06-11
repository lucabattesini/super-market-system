from fastapi import FastAPI
from routers import product_info, product_stock

app = FastAPI()

app.include_router(product_info.router)
app.include_router(product_stock.router)