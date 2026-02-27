# Inventory Management Logic 
from db import get_all_electronics, get_all_perishable, add_electronic, add_perishables, create_db
from models import Products, Electronics, Perishables

create_db()

class Inventory:
    def __init__(self):
        self.electronics = {}
        self.perishables = {}

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
        add_electronic(electronic.name, electronic.price, electronic.stock_quantity, electronic.warranty_period)
        
    def add_perishable(self, perishable):
        add_perishables(perishable.name, perishable.price, perishable.stock_quantity, perishable.expiration_date)

        

i = Inventory()
i.add_perishable(Perishables(1,"Apples",4,10,"02-10-2026"))
i.add_electronic(Electronics(1,"TV",500,10,3))
print(i.list_all_products())

