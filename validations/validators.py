from db.connection import cursor, connection
from repository.product_info_repository import create_product
from repository.product_stock_repository import create_product_in_stock

def check_if_id_already_exist(id, table):
    '''
    Check if an id already exists in an specific table
    '''
    cursor.execute("SELECT * FROM %s", (table))
    ids_list = cursor.fetchall()
    id_exists = int(0)
    for r in ids_list:
        if r == id:
            id_exists = id_exists + 1
    if id_exists == 0:
        return False
    elif id_exists > 0:
        return True
    

def create_product_in_both_tables(id, bar_code, name, price, description, category, brand, weight, unit, is_active):
    '''
    Will create a product in both tables wich depends from each other
    '''
    check_info_table = check_if_id_already_exist(id, "product_info")
    check_stock_table = check_if_id_already_exist(id, "product_stock")
    if check_info_table == False:
        if check_stock_table == False:
            create_product(id, name, price, description, category, brand, weight, unit, is_active)
            create_product_in_stock(id, bar_code)
            return {"message": "Product successfully created"}
        else:
            return {"message": "ID already exist"}
    else: 
        return {"message": "ID already exist"}