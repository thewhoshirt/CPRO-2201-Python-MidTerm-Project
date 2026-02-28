# Database connectivity and queries

import sqlite3 
from models import Products, Electronics, Perishables, Sales

def create_db():
    conn = sqlite3.connect("inventory.db")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def connect():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


# -------------------------
# Get products, electronics and produce 
# -------------------------
def get_all_product() -> list[Products]:
    with connect() as conn:
        rows = conn.execute("""SELECT product_id, name, price, stock_quantity FROM Products""").fetchall()

    return [Products(r["product_id"], r["name"], r["price"], r["stock_quantity"]) for r in rows]

def get_all_electronics() -> list[Electronics]:
    with connect() as conn: 
        rows = conn.execute("""
            SELECT p.product_id, p.name, p.price, p.stock_quantity, e.warranty_period
            FROM Products p
            JOIN Electronics e ON e.product_id = p.product_id
            ORDER BY p.product_id 
        """).fetchall()

    return [Electronics(r["product_id"], r["name"], r["price"], r["stock_quantity", r["warranty_period"]]) for r in rows]

def get_all_perishable() -> list[Perishables]:
    with connect() as conn: 
        rows = conn.execute("""
            SELECT p.product_id, p.name, p.price, p.stock_quantity, per.expiration_date
            FROM Products p
            JOIN Perishables per ON per.product_id = p.product_id
            ORDER BY p.product_id 
        """).fetchall()

    return [Perishables(r["product_id"], r["name"], r["price"], r["stock_quantity", r["expiration_date"]]) for r in rows]

# -------------------------
# Add to electronics and produce 
# -------------------------
def add_electronic(name:str, price:int, stock_quantity:int, warranty_period:int) -> int | None:
    try: 
        with connect() as conn:
            cur = conn.cursor()
            # Inserts into Products
            cur.execute(
                "INSERT INTO Products(name, price, stock_quantity) VALUES(?,?,?)", (name, price, stock_quantity) 
            )
        #Generates a new ID for product 
        new_product_id = cur.lastrowid
        
        #Inserts into Electronics
        cur.execute(
            "INSERT INTO Electronics(product_id, warranty_period) VALUES (?,?)", (new_product_id, warranty_period)
        )

        #Returns Product 
        return new_product_id
    
    #Error code, prints error and doesn't add to database 
    except sqlite3.IntegrityError as e: 
        print("Electronic Product Could Not Be Added: ", e)
        return None

def add_perishables(name:str, price:int, stock_quantity:int, expiration_date:int) -> int | None:
    try: 
        with connect() as conn:
            cur = conn.cursor()
            # Inserts into Products
            cur.execute(
                "INSERT INTO Products(name, price, stock_quantity) VALUES(?,?,?)", (name, price, stock_quantity) 
            )
        #Generates a new ID for product 
        new_product_id = cur.lastrowid
        
        #Inserts into perishables table 
        cur.execute(
            "INSERT INTO Perishables(product_id, expiration_date) VALUES (?,?)", (new_product_id, expiration_date)
        )

        #Returns Product 
        return new_product_id
    
    except sqlite3.IntegrityError as e: 
        print("Perishable Product Could Not Be Added: ", e)
        return None

# def delete_product(product_id):
    