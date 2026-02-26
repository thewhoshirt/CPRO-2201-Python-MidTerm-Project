-- Table Creation Script

-- Required Tables
-- • Products
-- • Electronics (for electronics-specific data)
-- • Perishables (for perishable-specific data)
-- • Sales (to store transaction history)

DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Electronics;
DROP TABLE IF EXISTS Perishables;
DROP TABLE IF EXISTS Sales;

CREATE TABLE Products(
    product_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL, 
    price INTEGER NOT NULL, 
    stock_quantity INTEGER 
)

CREATE TABLE Electronics(
    product_id INTEGER PRIMARY KEY NOT NULL,
    warranty_period INTEGER, 

    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
-- Perishables Table 
CREATE TABLE Perishabless(
    product_id INTEGER PRIMARY KEY NOT NULL,
    expiration_date TEXT, 

    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)


CREATE TABLE Sales(
    sales_id INTEGER PRIMARY KEY NOT NULL, 
    product_id INTEGER NOT NULL,
    price INTEGER NOT NULL,

    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)