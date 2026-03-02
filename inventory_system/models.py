# Product and Sale classes
from dataclasses import dataclass

@dataclass
class Products:
    product_id: int
    name: str
    price: int
    stock_quantity: int


    # -------------------------
    # Update price
    # -------------------------
    def update_price(self, new_price):
        self.price = new_price

    # -------------------------
    # Automatically update stock
    # -------------------------
    def update_stock(self, quantity):
        if self.is_in_stock():
            self.stock_quantity = self.stock_quantity - quantity
            
            if not self.is_in_stock():
                self.stock_quantity = self.stock_quantity + quantity
                return "Out of stock"
            else:
                return self.stock_quantity
        else:
            self.stock_quantity = self.stock_quantity + quantity
            return "Out of stock"

    # -------------------------
    # Check if product is in stock
    # -------------------------
    def is_in_stock(self):
        if self.stock_quantity > 0:
            return True
        else:
            return False
        
    # -------------------------
    # Get nicely displayed product details
    # -------------------------
    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity}"

@dataclass
class Electronics(Products):
    warranty_period: int

    # -------------------------
    # Get nicely displayed product details with warranty
    # -------------------------
    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity} | Warranty period: {self.warranty_period}"

@dataclass
class Perishables(Products):
    expiration_date: str

    # -------------------------
    # Get nicely displayed product details with expiration date
    # -------------------------
    def get_product_details(self):
        return f"Product id: {self.product_id} | Name: {self.name} | Price: {self.price} | Quantity: {self.stock_quantity} | Expiration date: {self.expiration_date}"

@dataclass
class Sales(Products):
    sales_id: int
    price: int

    # -------------------------
    #  Managing a sale
    # -------------------------
    def sale(self, product, quantity):
        sale = product.update_stock(quantity)
        if sale != "Out of stock":
            self.price = product.price * quantity
            return self.price
        else:
            return sale
