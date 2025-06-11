from connection import cursor

# Create a table
cursor.execute("CREATE TABLE product_info (id VARCHAR(36) PRIMARY KEY, name VARCHAR(100), price DECIMAL(10, 2), description TEXT, category VARCHAR(50), brand VARCHAR(50), weight DECIMAL(10, 2), unit VARCHAR(10), is_active BOOLEAN);")

cursor.execute("CREATE TABLE product_stock (bar_code TEXT PRIMARY KEY, product_id TEXT NOT NULL, overall_stock INTEGER NOT NULL DEFAULT 0, store_stock INTEGER NOT NULL DEFAULT 0, warehouse_stock INTEGER NOT NULL DEFAULT 0);")