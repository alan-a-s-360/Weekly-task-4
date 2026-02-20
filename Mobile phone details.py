class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self, discount_amount):
        if discount_amount > 0:
            if discount_amount <= self.price:
                self.price -= discount_amount
                print(f"Discount of ${discount_amount} applied.")
            else:
                print("Discount amount cannot exceed the price.")
        else:
            print("Discount amount must be positive.")
    def display_mobile(self):
        print("----- Mobile Details -----")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print("---------------------------")
mobile1 = Mobile("Apple", "iPhone 14", 999)
mobile1.display_mobile()
mobile1.apply_discount(100)
mobile1.display_mobile()                                                                                                                                                                                                                           Q3
