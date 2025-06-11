from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repository.product_info_repository import create_product, get_all_products, delete_product
from schemas.products_info_schema import ProductInfo

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
    products = get_all_products()
    paginated_products = products[skip: skip + limit]
    json_result = jsonable_encoder(paginated_products)
    return JSONResponse(
        content={
            "data": json_result,
            "total": len(products),
            "skip": skip,
            "limit": limit
        },
        status_code=status.HTTP_200_OK
    )

@router.post("/")
async def create_product_route(product: ProductInfo):
    '''
    Route used to create a new product
    '''
    create_product(product.id, product.name, product.price, product.description, product.category, product.brand, product.weight, product.unit, product.is_active)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product created successfully"}
    )

@router.put("/")
async def edit_product_route(product: ProductInfo):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product edited successfully"}
    )

@router.delete("/{id}")
async def delete_product_route(id):
    '''
    Route used to delete a product
    '''
    delete_product(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product deleted successfully"}
    )