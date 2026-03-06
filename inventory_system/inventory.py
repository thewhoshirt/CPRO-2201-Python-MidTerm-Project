# Inventory Management Logic 
from db import (get_all_electronics, get_all_perishable, add_electronic, add_perishables, 
                delete_product, update_price, update_stock,add_sale, get_all_sales)
from models import Electronics, Perishables, Sales

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
    # Get electronics and perishables into displayable format - and sales 
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

        display_list.append("---------------")
        display_list.append("Sales")
        display_list.append("---------------")
        sales_details = self.display_sales()
        if sales_details:
            for detail in sales_details:
                display_list.append(detail)
        else:
            display_list.append('No sales currently')

        return display_list
    
    # -------------------------
    # Add new products
    # -------------------------
    def add_electronic(self, name, price, stock, warranty):
        add_electronic(name, price, stock, warranty)

        
    def add_perishable(self, name, price, stock, date):
        add_perishables(name, price, stock, date)

    # -------------------------
    # Delete product
    # -------------------------
    def delete_product(self, product_id):
        delete_product(product_id)


    # -------------------------
    # Update product
    # -------------------------
    def update_price(self, product, new_price):
        product.update_price(new_price)
        update_price(product.product_id, new_price)


    def update_stock(self, product, quantity):
        in_stock = product.update_stock(quantity)
        if in_stock == False:
            self.list_all_products()
            return False
        else:
            update_stock(product.product_id, in_stock)
            return in_stock
        
    def user_update_stock(self, product, quantity):
        product.stock_quantity = quantity
        update_stock(product.product_id, quantity)

    # -------------------------
    # Managing a sale
    # -------------------------
    def sale(self, product, quantity):
        in_stock = self.update_stock(product, quantity)
        if in_stock:
            sale = Sales(product.product_id, 1, quantity, product.price * quantity)

            add_sale(sale.product_id, sale.quantity, sale.price)

        else:
            return "Not enough stock item in stock."
        

    def display_sales(self):
        self.sales.clear()
        all_sales = get_all_sales()
        for s in all_sales:
            self.sales.append(Sales(s.sales_id, s.product_id, s.quantity, s.price).get_sales_details())
        return self.sales



