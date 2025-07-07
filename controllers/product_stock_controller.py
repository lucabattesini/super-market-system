from repository.product_stock_repo import edit_product_quantity_in_stock
from repository.product_stock_repo import edit_product_quantity_in_stock, get_product_id_by_bar_code

def edit_different_products_quantity_in_stock(products):
    for r in products:
        bar_code = r["bar_code"]
        quantity = r["quantity"]
        id = get_product_id_by_bar_code(bar_code)
        edit_product_quantity_in_stock(id, quantity, "sub")
    return {"message": "products edited successfully"}