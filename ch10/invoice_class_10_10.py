# This program will create an Invoice class


from decimal import Decimal

class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self._part_number = part_number
        self._part_description = part_description
        self.quantity = quantity
        self.price_per_item = price_per_item
    
    @property
    def part_number(self):
        return self._part_number
    
    @part_number.setter
    def part_number(self, value):
        self._part_number = value

    @property
    def part_description(self):
        return self._part_description
    
    @part_description.setter
    def part_description(self, value):
        self._part_description = value

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity can't be negative")
        self._quantity = value

    @property
    def price_per_item(self):
        return self._price_per_item
    
    @price_per_item.setter
    def price_per_item(self, value):
        if value < 0:
            raise ValueError("Price per item can't be negative")
        self._price_per_item = Decimal(value)

    def calculate_invoice(self):
        return self.quantity * self.price_per_item

    def __repr__(self):
        return f"Invoice(part_number={self.part_number}, part_description={self.part_description}, quantity={self.quantity}, price_per_item={self.price_per_item})"
