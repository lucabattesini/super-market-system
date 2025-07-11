from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import repository.product_info_repo as product_info_repo
from schemas.products_info_schema import ProductInfo
from schemas.products_stock_schema import ProductStock
from controllers.product_info_controller import get_all_products, get_product_by_id, create_product_in_both_tables, delete_product_in_both_tables


router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_products_route():
    '''
    Route used to return all the products
    '''
    products = await get_all_products()
    return JSONResponse(
        content={
            "data": products,
            "total": len(products),
        },
        status_code=status.HTTP_200_OK
    )

@router.get("/{id}")
async def get_product_by_id_route(id):
    product = await get_product_by_id(id)
    return JSONResponse(
        content={
            "data": product
        },
        status_code=status.HTTP_200_OK
    )

@router.post("/")
async def create_product_route(product: ProductInfo, stock: ProductStock):
    '''
    Route used to create a new product
    '''
    create_product_in_both_tables(stock.bar_code, product.name, product.price, product.description, product.category, product.brand, product.weight, product.unit, product.is_active)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Product created successfully"}
    )

@router.put("/")
async def edit_product_route(product: ProductInfo):
    '''
    Route used to edit a product
    '''
    product_info_repo.edit_product(product.id, product.name, product.price, product.description, product.category, product.brand, product.weight, product.unit, product.is_active)
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"message": "Product edited successfully"}
    )

@router.delete("/{id}")
async def delete_product_route(id):
    '''
    Route used to delete a product
    '''
    delete_product_in_both_tables(id)
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"message": "Product deleted successfully"}
    )