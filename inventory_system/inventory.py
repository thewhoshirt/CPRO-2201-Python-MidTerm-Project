# Inventory Management Logic 
from db import get_all_electronics, get_all_perishable, get_all_product
from models import Products, Electronics, Perishables

class Inventory:
    def __init__(self):
        self.electronics = {}
        self.perishables = {}

    # -------------------------
    # Get electronics and perishables from database
    # -------------------------
    def retrieve_products(self):
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

        print(display_list)


        

i = Inventory()
i.list_all_products()

