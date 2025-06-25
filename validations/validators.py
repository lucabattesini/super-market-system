from db.connection import cursor, connection
from repository.product_info_repository import create_product
from repository.product_stock_repository import create_product_in_stock

def create_product_in_both_tables():
    return

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