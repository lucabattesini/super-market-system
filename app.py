from fastapi import FastAPI
from routers import product_info_router, product_stock_router

app = FastAPI()

app.include_router(product_info_router.router)
app.include_router(product_stock_router.router)