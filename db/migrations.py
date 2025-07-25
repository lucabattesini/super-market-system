from connection import cursor

# Create the main tables
cursor.execute("CREATE TABLE product_info (id VARCHAR(36) PRIMARY KEY, name VARCHAR(100), price DECIMAL(10, 2), description TEXT, category VARCHAR(50), brand VARCHAR(50), weight DECIMAL(10, 2), unit VARCHAR(10), is_active BOOLEAN);")

cursor.execute("CREATE TABLE product_stock (id VARCHAR(50) NOT NULL, bar_code VARCHAR(50) NOT NULL UNIQUE, overall_stock INT NOT NULL, store_stock INT NOT NULL, warehouse_stock INT NOT NULL, last_updated DATETIME NOT NULL, PRIMARY KEY (id));")