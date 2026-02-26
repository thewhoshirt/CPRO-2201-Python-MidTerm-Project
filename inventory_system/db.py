# Database connectivity and queries

import sqlite3 
from models import Products, Electronics, Perishables, Sales

def connect():
    conn = sqlite3.connect('inventory.db')
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
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

    return [Electronics(r["product_id"], r["name"], r["price"], r["stock_quantity"], r["warranty_period"]) for r in rows]

def get_all_perishable() -> list[Perishables]:
    with connect() as conn: 
        rows = conn.execute("""
            SELECT p.product_id, p.name, p.price, p.stock_quantity, per.expiration_date
            FROM Products p
            JOIN Perishables per ON per.product_id = p.product_id
            ORDER BY p.product_id 
        """).fetchall()

    return [Perishables(r["product_id"], r["name"], r["price"], r["stock_quantity"], r["expiration_date"]) for r in rows]

