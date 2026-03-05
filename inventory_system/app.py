# User Interface
import inventory
import db
import tkinter as tk 
from tkinter import messagebox


# --------------------
# Electronics 
# --------------------

def add_electronic_click():
    pass 

def update_electronic_click():
    pass

def delete_electronic_click():
    pass

# --------------------
# Perishables
# --------------------

def add_perishable_click():
    pass 

def update_perishable_click():
    pass

def delete_perishable_click():
    pass


# --------------------
# APP START
# --------------------
db.create_db() 

root = tk.Tk()
root.title("Midterm Group Project - Inventory and Sales Management System")
root.geometry("1920x1080")

left = tk.Frame(root)
left.pack(side="left", padx=15, pady=15)

right = tk.Frame(root)
right.pack(side="right", padx=15, pady=15, fill="both", expand=True)

# ----- Products List ------

# -- Electronic --
tk.Label(left, text="ELECTRONICS", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(left, text="Product Name").pack()
electronic_name = tk.Entry(left, width=35)
electronic_name.pack()

tk.Label(left, text="Price").pack()
electronic_price = tk.Entry(left, width=35)
electronic_price.pack()

tk.Label(left, text="Stock").pack()
electronic_stock = tk.Entry(left, width=35)
electronic_stock.pack()

tk.Label(left, text="Warranty Period").pack()
electronic_warranty = tk.Entry(left, width=35)
electronic_warranty.pack()

#-- electronic buttons 
tk.Button(left, text="Add Electronic",
command=add_electronic_click).pack(pady=3)
tk.Button(left, text="Update Electronic",
command=update_electronic_click).pack(pady=2)
tk.Button(left, text="Delete Electronic",
command=delete_electronic_click).pack(pady=2)

# -- Perishables --
tk.Label(left, text="PERISHABLES ", font=("Arial", 12, "bold")).pack(pady=5)

tk.Label(left, text="Product Name").pack()
perishable_name = tk.Entry(left, width=35)
perishable_name.pack()

tk.Label(left, text="Price").pack()
perishable_price = tk.Entry(left, width=35)
perishable_price.pack()

tk.Label(left, text="Stock").pack()
perishable_stock = tk.Entry(left, width=35)
perishable_stock.pack()

tk.Label(left, text="Expiration Date").pack()
perishable_expiration = tk.Entry(left, width=35)
perishable_expiration.pack()

#-- perishables buttons 
tk.Button(left, text="Add Perishable",
command=add_perishable_click).pack(pady=3)
tk.Button(left, text="Update Perishable",
command=update_perishable_click).pack(pady=2)
tk.Button(left, text="Delete Perishable",
command=delete_perishable_click).pack(pady=2)

#-- perishables buttons 
tk.Button(left, text="Add Perishable",
command=add_perishable_click).pack(pady=3)
tk.Button(left, text="Update Perishable",
command=update_perishable_click).pack(pady=2)
tk.Button(left, text="Delete Perishable",
command=delete_perishable_click).pack(pady=2)



root.mainloop()