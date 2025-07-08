from db.connection import cursor, connection
from schemas.products_info_schema import ProductInfo

def parse_products(params) -> ProductInfo:
    '''
    Organize the vars into an object format
    '''
    return ProductInfo(
        id=params[0],
        name=params[1],
        price=params[2],
        description=params[3],
        category=params[4],
        brand=params[5],
        weight=params[6],
        unit=params[7],
        is_active=params[8]
    )

def get_all_products():
    '''
    Get all products from db and organize using parse_products()
    '''
    cursor.execute("SELECT * FROM product_info")
    unorganized_list = cursor.fetchall()
    organized_list = []
    for r in unorganized_list:
        organized_list.append(parse_products(r))
    return organized_list

def get_product_by_id(id):
    '''
    Get an specific product by it's id
    '''
    cursor.execute("SELECT * FROM product_info WHERE id = %s", (id,))
    row = cursor.fetchone()
    if row:
        return parse_products(row)
    return None

def create_product(id, name, price, description, category, brand, weight, unit, is_active):
    '''
    Create a product
    '''
    cursor.execute("INSERT INTO product_info (id, name, price, description, category, brand, weight, unit, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (id, name, price, description, category, brand, weight, unit, is_active)
                   )
    return {"message": "Product successfully created"}

def delete_product(id):
    '''
    Delete a product
    '''
    cursor.execute(f"DELETE FROM product_info WHERE id = '{id}'")

def edit_product(id, name, price, description, category, brand, weight, unit, is_active):
    '''
    Edit a product
    '''
    cursor.execute(f"UPDATE product_info SET name = '{name}', price = '{price}', description = '{description}', category = '{category}', brand = '{brand}', weight = '{weight}', unit = '{unit}', is_active = {is_active} WHERE id = '{id}';")
    connection.commit()
    return {"message": "Product successfully edited"}