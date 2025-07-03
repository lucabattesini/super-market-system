from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from repository.product_stock_repo import get_all_products_from_stock
from schemas.products_stock_schema import ProductStock
from typing import Literal

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_inventory_info_route():
    products = get_all_products_from_stock()
    return products

@router.put("/{operation}")
async def edit_product_stock_quantity_route(operation: Literal["add", "sub"], product: ProductStock):
    return