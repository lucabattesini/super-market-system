from fastapi import APIRouter, status
from typing import List
from fastapi.responses import JSONResponse
from repository.product_stock_repo import edit_product_quantity_in_stock
from schemas.products_stock_schema import ProductStockOperation, ProductStockBuyOperation
from controllers.product_stock_controller import edit_different_products_quantity_in_stock, get_all_products_from_stock_json

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_inventory_info_route():
    products = get_all_products_from_stock_json()
    return JSONResponse(
        content={
            "data": products
        },
        status_code=status.HTTP_200_OK
    )

@router.put("/")
async def edit_product_quantity_in_stock_route(product: ProductStockOperation):
    edit_product_quantity_in_stock(product.id, product.data, product.operation)
    return JSONResponse(
        content={
            "message": "successful operation"
        },
        status_code=status.HTTP_202_ACCEPTED
    )

@router.put("/buy-operation")
async def edit_different_products_quantity_in_stock_route(product: List[ProductStockBuyOperation]):
    edit_different_products_quantity_in_stock(product)
    return JSONResponse(
        content={
            "message": "successful operation"
        },
        status_code=status.HTTP_202_ACCEPTED
    )