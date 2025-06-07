# 9. Product with __eq__ method
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price


p1 = Product("Pen", 10)
p2 = Product("Pencil", 10)
print("Products are equal in price?" , p1 == p2)