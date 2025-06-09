from connection import cursor

# Create a table
cursor.execute("CREATE TABLE product_info (id, name, price, description, category, brand, weight, unit, is_active)")