# User Interface
import inventory 
import db
import tkinter as tk 
from tkinter import messagebox




inv = inventory.Inventory()
# --------------------
# Products
# --------------------

#has it not selecting any products at open 
selected_product_id = None

# refreshes list when items are added, deletes, updated, the window is opened or a sale is added 
def refresh_list():
    listbox_products.delete(0, tk.END)
    for p in inv.list_all_products():
        listbox_products.insert(tk.END, p)

def on_product_select(event):
    global selected_product_id

    sel = listbox_products.curselection()
    if not sel:
        return

    row = listbox_products.get(sel[0])
    try:
        # splits the string so we can correctly select a product ID for a sale 
        product_id_str = row.split("|")[0].split(":")[1].strip()
        selected_product_id = int(product_id_str)
    except(ValueError, IndexError):
        selected_product_id=None




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
# Sales
# --------------------
def add_sale_click():
    global selected_product_id

    #Check for if product is selected 
    if selected_product_id is None: 
        messagebox.showerror("Error", "No Product Selected, Please Select a Product")
        return
    # finding product in Inventory
    product = inv.electronics.get(selected_product_id) or inv.perishables.get(selected_product_id)

    if product is None:
        messagebox.showerror("Error", "Product Not Found")
        return
    
    #Create Sale Window 
    sale_window = tk.Toplevel(root)
    sale_window.title("Purchase Product")
    sale_window.geometry("300x150")

    tk.Label(sale_window, text="Enter Quantity:").pack()
    quantity_entered = tk.Entry(sale_window, width=20)
    quantity_entered.pack(pady=5)

    # creates a var to display the product price, that can be updated as the quantity increases 
    price_var = tk.StringVar()
    price_var.set(f"Total Price: {product.price}")
    tk.Label(sale_window, textvariable=price_var).pack(pady=5)

    #Updates/displays price of purchases in the sales window 
    def update_price(*args):
        try:
            qty = int(quantity_entered.get())
            total = product.price * qty
            price_var.set(f"Total Price: {total}")
        except ValueError:
            price_var.set(f"Total Price: {product.price}")
    quantity_entered.bind("<KeyRelease>", update_price)
   
    #Buy Button function 
    def on_buy():
        try:
            quantity = int(quantity_entered.get())
            if quantity <=0:
                messagebox.showerror("Error","Quantity must be greater than 0.")
            elif quantity > product.stock_quantity:
                messagebox.showerror("Error", f"Not enough stock. Available stock: {product.stock_quantity}.")
                return
            else:
                inv.sale(product, quantity)
                messagebox.showinfo("Success", f"Purchased {quantity} units of {product.name}")
                refresh_list()
                sale_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    def on_cancel():
       sale_window.destroy()
    
    #-- Sale Windows Buttons 
    button_frame = tk.Frame(sale_window)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Cancel", command=on_cancel, width=10).pack(side="left", padx=5)
    tk.Button(button_frame, text="Buy", command=on_buy, width=10).pack(side="left", padx=5)

# --------------------
# APP START
# --------------------


root = tk.Tk()
root.title("Midterm Group Project - Inventory and Sales Management System")
root.geometry("1150x820")

left = tk.Frame(root)
left.pack(side="left", padx=15, pady=15)

right = tk.Frame(root)
right.pack(side="right", padx=15, pady=15, fill="both", expand=True)

# ----- Products List ------

# --------------------
# ELECTRONS 
# --------------------
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


tk.Label(left, text=" ").pack()

# --------------------
# PERISHABLES
# --------------------
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

# --------------------
# LISTBOX
# --------------------

tk.Label(right, text="Products Table", font=("Arial", 12, "bold")).pack()
listbox_products = tk.Listbox(right, width=130, height=30)
listbox_products.pack(pady=6)
listbox_products.bind("<<ListboxSelect>>", on_product_select)

tk.Button(right, text="Buy Product", command=add_sale_click).pack(pady=6)

refresh_list()
root.mainloop()