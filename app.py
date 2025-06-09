from fastapi import FastAPI
from routers import product_info

app = FastAPI()

app.include_router(product_info.router)