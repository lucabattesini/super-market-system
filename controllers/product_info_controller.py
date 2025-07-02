import repository.product_info_repo as product_info_repo
from fastapi.encoders import jsonable_encoder
from repository.product_info_repo import create_product
from repository.product_stock_repo import create_product_in_stock
from uuid import uuid1

async def get_all_products():
    '''
    Function used to return all the products
    '''
    products = product_info_repo.get_all_products()
    json_result = jsonable_encoder(products)
    return json_result

async def get_product_by_id(id):
    '''
    Function used to return and product selected by id
    '''
    product = product_info_repo.get_product_by_id(id)
    json_result = jsonable_encoder(product)
    return json_result

def create_product_in_both_tables(bar_code, name, price, description, category, brand, weight, unit, is_active):
    '''
    Will create a product in both tables which depends from each other
    '''
    id = str(uuid1())
    create_product(id, name, price, description, category, brand, weight, unit, is_active)
    create_product_in_stock(id, bar_code)
    return {"message": "Product successfully created"}