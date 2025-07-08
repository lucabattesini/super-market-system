from fastapi.encoders import jsonable_encoder
from repository.product_stock_repo import edit_product_quantity_in_stock, get_product_id_by_bar_code, edit_product_quantity_in_stock, get_all_products_from_stock

def edit_different_products_quantity_in_stock(products):
    '''
    Edit different products quantity in stock
    '''
    for r in products:
        bar_code = r.bar_code
        quantity = r.quantity
        id = str(get_product_id_by_bar_code(bar_code))
        edit_product_quantity_in_stock(id, quantity, "sub")
    return {"message": "Products edited successfully"}

def get_all_products_from_stock_json():
    '''
    Turn all data goten into json format
    '''
    products = get_all_products_from_stock()
    json_result = jsonable_encoder(products)
    return json_result