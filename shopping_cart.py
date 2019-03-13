class ShoppingCart():
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        self.all_items_price = []
        self.items_price = []
        self.items_quantity = []

        
    def add_item(self, name, price, quantity=1):
        self.items.append(name)
        self.items_price.append(price)
        self.items_quantity.append(quantity)
        
        for i in range(quantity):
            self.all_itmes_price.append(price)
        
        total = price * quantity
        self.total += total
        return self.total
   
    def mean_item_price(self):
        return self.total / sum(self.items_quantity)

    def median_item_price(self):
        if len(self.all_items_price) % 2: #odd
            median_position = len(self.all_items_price) / 2
            return self.all_items_price[median_position]
        else: #even
            low_med_pos = len(self.all_items_price) / 2 - 1
            upp_med_pos = len(self.all_items_price) / 2 
            return (self.all_items_price[low_med_pos] + self.all_items_price[upp_med_pos]) / 2
            

    def apply_discount(self):
        if not self.employee_discount:
            return "sorry, there is no discount to apply to your cart :("
        else:
            discount = (100 - self.employee_discount) * 0.01
            total_w_discount = self.total * discount
            return total_w_discount

    def void_last_item(self):
        if len(self.items) < 1:
            return "There are no items in your cart!"
        else:
            total = self.items_price.pop() * self.items_quantity.pop()
            self.total -= total
            self.items.pop()
            
