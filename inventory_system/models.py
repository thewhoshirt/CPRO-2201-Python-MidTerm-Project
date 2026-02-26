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
        
    # def sell(self, quantity):
        

@dataclass
class Electronics(Products):
    warranty_period: int

@dataclass
class Perishables(Products):
    expiration_date: str

@dataclass
class Sales:
    sales_id: int
    price: int