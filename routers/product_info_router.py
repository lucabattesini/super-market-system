from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import repository.product_info_repo as product_info_repo
from schemas.products_info_schema import ProductInfo
from controllers.product_info_controller import get_all_products


router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_all_products_route(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1)):
    '''
    Route used to return all the products
    '''
    products = await get_all_products(skip, limit)
    return products

@router.post("/")
async def create_product_route(product: ProductInfo):
    '''
    Route used to create a new product
    '''
    product_info_repo.create_product(product)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product created successfully"}
    )

@router.put("/")
async def edit_product_route(product: ProductInfo):
    '''
    Route used to edit a product
    '''
    product_info_repo.edit_product(product.id, product.name, product.price, product.description, product.category, product.brand, product.weight, product.unit, product.is_active)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product edited successfully"}
    )

@router.delete("/{id}")
async def delete_product_route(id):
    '''
    Route used to delete a product
    '''
    product_info_repo.delete_product(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product deleted successfully"}
    )