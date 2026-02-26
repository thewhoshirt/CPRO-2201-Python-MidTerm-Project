# Product and Sale classes
from dataclasses import dataclass

@dataclass
class Products:
    product_id: int
    name: str
    price: int
    stock_quantity: int

    def update_price(self, new_price):
        self.price = new_price

    def update_stock(self, quantity):
        self.stock_quantity = quantity

    def is_in_stock(self, quantity):
        if quantity > 0:
            return True
        else:
            return False
        
    def sell(self, quantity):
        self.stock_quantity -= quantity

    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity}"

@dataclass
class Electronics(Products):
    warranty_period: int

    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity} | Warranty period: {self.warranty_period}"

@dataclass
class Perishables(Products):
    expiration_date: str

    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity} | Expiration date: {self.expiration_date}"

@dataclass
class Sales(Products):
    sales_id: int
    price: int

    def sale(self, product, quantity):
        try:
            product.stock_quantity -= quantity
            self.price = product.price * quantity
            return self.price
        except Exception:
            return "Insufficient quantity"