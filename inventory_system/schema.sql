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


/* -------------------------
   Create Tables 
*/ -------------------------

-- Products Table
CREATE TABLE Products(
    product_id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL, 
    price INTEGER NOT NULL, 
    stock_quantity INTEGER NOT NULL
);

-- Electronics Table
CREATE TABLE Electronics(
    product_id INTEGER PRIMARY KEY NOT NULL,
    warranty_period INTEGER NOT NULL, 
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);
-- Perishables Table 
CREATE TABLE Perishables(
    product_id INTEGER PRIMARY KEY NOT NULL,
    expiration_date TEXT, 
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

-- Sales Table 
CREATE TABLE Sales(
    sales_id INTEGER PRIMARY KEY NOT NULL, 
    product_id INTEGER NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

/* -------------------------
   Populate tables 
*/ -------------------------
INSERT INTO Products(product_id, name, price, stock_quantity)
    VALUES(1, "Laptop", 1200, 4);

INSERT INTO Electronics(product_id, warranty_period)
    VALUES(1, 8);

INSERT INTO Products(product_id, name, price, stock_quantity)
    VALUES(2, "Phone", 1000, 10);

INSERT INTO Electronics(product_id, warranty_period)
    VALUES(2, 3);

INSERT INTO Products(product_id, name, price, stock_quantity)
    VALUES(3, "Banana", 10, 50);

INSERT INTO Perishables(product_id, expiration_date)
    VALUES(3, 5);