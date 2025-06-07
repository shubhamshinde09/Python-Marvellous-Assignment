# 3 Book class with private attribute
class Book:
    def __init__(self, price):
        self.__price = price  # private attribute

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


b = Book(500)
print("Price:", b.get_price())
b.set_price(600)
print("Updated Price:", b.get_price())