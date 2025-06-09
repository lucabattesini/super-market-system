from db.connection import cursor, connection

def create_product(id, name, price, description, category, brand, weight, unit, is_active):
    '''
    Create a product
    '''
    cursor.execute("INSERT INTO product_info (id, name, price, description, category, brand, weight, unit, is_active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, name, price, description, category, brand, weight, unit, is_active)
                   )
    connection.commit