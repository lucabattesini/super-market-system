from db.connection import cursor, connection
from schemas.products_stock_schema import ProductStock

def parse_product_from_stock(params) -> ProductStock:
    '''
    Organize the vars into an object format
    '''
    return ProductStock(
        product_id=params[0],
        bar_code=params[1],
        overall_stock=params[2],
        store_stock=params[3],
        warehouse_stock=params[4]
        )

def get_all_products_from_stock():
    return

def disable_product_from_stock():
    return

def create_product_in_stock():
    return

def edit_product_stock_quantity():
    return