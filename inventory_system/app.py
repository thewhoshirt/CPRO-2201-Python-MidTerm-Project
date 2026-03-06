# User Interface
import inventory 
import tkinter as tk 
from tkinter import messagebox
from datetime import datetime

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

# clears all text box fields
def clear_fields():
    electronic_name.delete(0,tk.END)
    electronic_price.delete(0,tk.END)
    electronic_stock.delete(0,tk.END)
    electronic_warranty.delete(0,tk.END)

    perishable_name.delete(0,tk.END)
    perishable_price.delete(0,tk.END)
    perishable_stock.delete(0,tk.END)
    perishable_expiration.delete(0,tk.END)

# gets the selected product from the table
def on_product_select(event):
    global selected_product_id

    sel = listbox_products.curselection()
    if not sel:
        return

    row = listbox_products.get(sel[0])
    try:
        if row.split(" ")[0] == "Sale":
            selected_product_id=None
            clear_fields()
            return
        
        # splits the string so we can correctly select a product ID for a sale 
        product_id_str = row.split("|")[0].split(":")[1].strip()
        selected_product_id = int(product_id_str)

        clear_fields()

        # finding product in Inventory
        if inv.electronics.get(selected_product_id) is not None:
            product = inv.electronics.get(selected_product_id)
            
            electronic_name.insert(0,product.name)
            electronic_price.insert(0,product.price)
            electronic_stock.insert(0,product.stock_quantity)
            electronic_warranty.insert(0,product.warranty_period)

        elif inv.perishables.get(selected_product_id) is not None:
            product = inv.perishables.get(selected_product_id)

            perishable_name.insert(0,product.name)
            perishable_price.insert(0,product.price)
            perishable_stock.insert(0,product.stock_quantity)
            perishable_expiration.insert(0,product.expiration_date)

    except(ValueError, IndexError):
        selected_product_id=None
        clear_fields()



# --------------------
# Electronics 
# --------------------

def add_electronic_click():
    name = electronic_name.get().strip()
    price = electronic_price.get().strip()
    stock = electronic_stock.get().strip()
    warranty = electronic_warranty.get().strip()

    # check if fields are filled out
    if not name or not price or not stock or not warranty:
        messagebox.showwarning("Missing", "All fields required.")
        return

    # checks datatypes of price, stock and warranty fields
    try:
        numbers = float(price), int(stock), int(warranty)
    except:
        messagebox.showwarning("Type", "Price, stock and warranty must be numbers.")
        return

    # checks if inputs are greater than 0
    if float(price) <= 0 or int(stock) < 0 or int(warranty) < 0:
        messagebox.showwarning("Invalid Price", "Price, stock quantity and warranty must be greater than 0.")
        return

    # add new product
    inv.add_electronic(name, price, stock, warranty)
    clear_fields()
    refresh_list()


def update_electronic_click():
    # checks if electroninc is selected
    electronic = inv.electronics.get(selected_product_id)
    if selected_product_id is None or electronic is None:
        messagebox.showwarning("No product", "Select an electronic.")
        return
    
    new_price = electronic_price.get().strip()
    new_stock = electronic_stock.get().strip()

    # checks datatype of price and stock
    try:
        numbers = float(new_price), int(new_stock)
    except:
        messagebox.showwarning("Type", "Price and stock quantity must be a number.")
        return
    
    # checks if inputs are greater than 0
    if float(new_price) <= 0 or int(new_stock) < 0:
        messagebox.showwarning("Invalid Price", "Price and stock quantity must be greater than 0.")
        return
    
    # updated price of electronic
    inv.update_price(electronic,new_price)
    inv.user_update_stock(electronic, new_stock)
    clear_fields()
    refresh_list()

def delete_electronic_click():
    # checks if electronic is selected
    electronic = inv.electronics.get(selected_product_id)
    if selected_product_id is None or electronic is None:
        messagebox.showwarning("No product", "Select an electronic.")
        return

    # deletes eletronic
    inv.delete_product(electronic.product_id)
    clear_fields()
    refresh_list()

# --------------------
# Perishables
# --------------------

def add_perishable_click():
    name = perishable_name.get().strip()
    price = perishable_price.get().strip()
    stock = perishable_stock.get().strip()
    expiration = perishable_expiration.get().strip()

    # checks if fields are filled out
    if not name or not price or not stock or not expiration:
        messagebox.showwarning("Missing", "All fields required.")
        return

    # checks datatype of price and stock
    try:
        numbers = float(price), int(stock)
    except:
        messagebox.showwarning("Type", "Price and stock must be numbers.")
        return
    
    # checks if inputs are greater than 0
    if float(price) <= 0 or int(stock) < 0:
        messagebox.showwarning("Invalid Price", "Price and stock quantity must be greater than 0.")
        return
    
    # checks if expiration is in the appropriate date format
    try:
        datetime.strptime(expiration, '%Y-%m-%d')
    except:
        messagebox.showwarning("Date", "Expiration date must be in format YYYY-MM-DD")
        return

    # adds new perishable
    inv.add_perishable(name, price, stock, expiration)
    clear_fields()
    refresh_list()

def update_perishable_click():
    # checks if perishable is selected
    perishable = inv.perishables.get(selected_product_id)
    if selected_product_id is None or perishable is None:
        messagebox.showwarning("No product", "Select a perishable.")
        return
    
    new_price = perishable_price.get().strip()
    new_stock = perishable_stock.get().strip()

    # checks if the inputs are a number
    try:
        numbers = float(new_price), int(new_stock)
    except:
        messagebox.showwarning("Type", "Price and stock quantity must be a number.")
        return
    
    # checks if inputs are greater than 0
    if float(new_price) <= 0 or int(new_stock) < 0:
        messagebox.showwarning("Invalid Price", "Price and stock quantity must be greater.")
        return
    
    # updates price
    inv.user_update_stock(perishable,new_stock)
    inv.update_price(perishable,new_price)
    clear_fields()
    refresh_list()

def delete_perishable_click():
    # checks if perishable is selected
    perishable = inv.perishables.get(selected_product_id)
    if selected_product_id is None or perishable is None:
        messagebox.showwarning("No product", "Select a perishable.")
        return

    # deletes perishable
    inv.delete_product(perishable.product_id)
    clear_fields()
    refresh_list()

# --------------------
# Sales
# --------------------
def add_sale_click():
    global selected_product_id
    clear_fields()

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
    price_var.set(f"Total Price: {product.price:.2f}")
    tk.Label(sale_window, textvariable=price_var).pack(pady=5)

    #Updates/displays price of purchases in the sales window 
    def update_price(*args):
        try:
            qty = int(quantity_entered.get())
            total = product.price * qty
            price_var.set(f"Total Price: {total:.2f}")
        except ValueError:
            price_var.set(f"Total Price: {product.price:.2f}")
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