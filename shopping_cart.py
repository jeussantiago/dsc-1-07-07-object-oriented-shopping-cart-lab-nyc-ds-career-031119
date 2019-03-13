class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        self.last_item_quantity = 0
        self.last_item_price = 0.0
        
    def add_item(self, name, price, quantity=1):
        self.items.append(name)
        self.last_item_price = price
        self.last_item_quantity = quantity
        total = price * quantity
        self.total += total
        return self.total
   
    def mean_item_price(self):
        return self.total / len(self.items)

    def median_item_price(self):
        pass

    def apply_discount(self):
        if not self.employee_discount:
            return "sorry, there is no discount to apply to your cart :("
        else:
            discount = (100 - self.employee_discount) * 0.01
            self.total = self.total * discount
            return self.total

    def void_last_item(self):
        if len(self.items) < 1:
            return "There are no items in your cart!"
        else:
            total = self.last_item_price * self.last_item_quantity
            self.total = self.total - total
            self.items.pop()