# Inventory Management Logic 
from db import (get_all_electronics, get_all_perishable, add_electronic, add_perishables, 
                delete_product, update_price, update_stock,add_sale, get_all_sales, create_db)
from models import Electronics, Perishables, Sales

# won't need? be in app.py instead?
create_db()

class Inventory:
    def __init__(self):
        self.electronics = {}
        self.perishables = {}
        self.sales = []

    # -------------------------
    # Get electronics and perishables from database
    # -------------------------
    def retrieve_products(self):
        self.electronics.clear()
        self.perishables.clear()

        electronics = get_all_electronics()
        perishable = get_all_perishable()


        for e in electronics:
            self.electronics[e.product_id] = Electronics(e.product_id, e.name, e.price, e.stock_quantity, e.warranty_period)

        for p in perishable:
            self.perishables[p.product_id] = Perishables(p.product_id, p.name, p.price, p.stock_quantity, p.expiration_date)
    
    # -------------------------
    # Get electronics and perishables into displayable format
    # -------------------------
    def list_all_products(self):
        self.retrieve_products()
        display_list = []
        
        display_list.append("---------------")
        display_list.append("Electronics")
        display_list.append("---------------")
        if len(self.electronics) > 0:
            for p in self.electronics.values():
                display_list.append(p.get_product_details())
        else:
            display_list.append("No electronics available")

        display_list.append("---------------")
        display_list.append("Perishables")
        display_list.append("---------------")
        if len(self.perishables) > 0:
            for p in self.perishables.values():
                display_list.append(p.get_product_details())
        else:
            display_list.append('No perishables available')

        return display_list
    
    # -------------------------
    # Add new products
    # -------------------------
    def add_electronic(self, electronic):
        try:
            add_electronic(electronic.name, electronic.price, electronic.stock_quantity, electronic.warranty_period)

            self.list_all_products()

            return "Product added successfully"
        except Exception:
            return "Product wasn't able to be added"
        
    def add_perishable(self, perishable):
        try:
            add_perishables(perishable.name, perishable.price, perishable.stock_quantity, perishable.expiration_date)

            self.list_all_products()

            return "Product added successfully"
        except Exception:
            return "Product wasn't able to be added"

    # -------------------------
    # Delete product
    # -------------------------
    def delete_product(self, product_id):
        try:
            delete_product(product_id)

            self.list_all_products()

            return "Deletion successful"
        except Exception:
            return "Deletion unsucceful"

    # -------------------------
    # Update product
    # -------------------------
    def update_price(self, product, new_price):
        try:
            product.update_price(new_price)
            update_price(product.product_id, new_price)

            self.list_all_products()
            return "Update successful"
        except Exception:
            return "Update unsuccessful"

    def update_stock(self, product, quantity):
        in_stock = product.update_stock(quantity)
        if in_stock == False:
            self.list_all_products()
            return False
        else:
            update_stock(product.product_id, in_stock)
            return in_stock

    # -------------------------
    # Managing a sale
    # -------------------------
    def sale(self, product, quantity):
        in_stock = self.update_stock(product, quantity)
        if in_stock != "Out of stock":
            sale = Sales(product.product_id, 1, quantity, product.price * quantity)
            try:
                add_sale(sale.product_id, sale.quantity, sale.price)

                return "Sale success."
            except Exception: 
                return "Sale unsuccessful."
        else:
            return "Not enough stock item in stock."
        

    def display_sales(self):
        self.sales.clear()
        all_sales = get_all_sales()
       
        if len(all_sales) > 0:
            for s in all_sales:
                self.sales.append(Sales(s.sales_id, s.product_id, s.quantity, s.price).get_sales_details())
            
            return self.sales

        else:
            return "No sales yet."


        
# # testing
# i = Inventory()
# e = Electronics(1,"TV",500,10,3)
# p = Perishables(1,"Apples",4,10,"02-10-2026")
# i.add_perishable(p)
# i.add_electronic(e)
# print(i.list_all_products())
# i.delete_product(1)
# print(i.list_all_products())

# i.update_price(e, 1000)
# print(e.get_product_details())
# i.update_stock(e, 2)
# print(e.get_product_details())
# print(e.update_stock(10))
# print(e.get_product_details())

# print(i.sale(p,10))
# print(i.display_sales())
# print(i.list_all_products())


