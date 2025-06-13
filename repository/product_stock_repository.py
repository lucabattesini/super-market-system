from db.connection import cursor, connection
from schemas.products_stock_schema import ProductStock

def parse_product_from_stock(params) -> ProductStock:
    '''
    Return the schema in a json format
    '''
    return ProductStock(
        product_id=params[0],
        bar_code=params[1],
        overall_stock=params[2],
        store_stock=params[3],
        warehouse_stock=params[4],
        last_updated=params[5],
        is_active=[6]
        )

def get_all_products_from_stock():
    '''
    Return all the products from stock
    '''
    cursor.execute("SELECT * FROM product_stock")
    unorganized_list = cursor.fetchall()
    organized_list = []
    for r in unorganized_list:
        organized_list.append(parse_product_from_stock(r))
    return organized_list

def disable_product_from_stock():
    '''
    Will disabe a product in product_stock table by changing a var name
    '''
    return

def create_product_in_stock():
    '''
    Create a product in stock
    '''
    return

def edit_product_stock_quantity(id, column, data, operation):
    '''
    Change the stock quantity of a product
    '''
    if operation == "add":
        cursor.execute(f"UPDATE product_stock SET {column} = {column} + {data} WHERE id = '{id}';")
    elif operation == "sub":
        cursor.execute(f"UPDATE product_stock SET {column} = {column} - {data} WHERE id = '{id}';")
    else:
        return KeyError
    return