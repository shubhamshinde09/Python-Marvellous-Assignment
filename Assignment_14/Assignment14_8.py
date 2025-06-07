# 8 Vehicle and Car (method overriding)
class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):
        print("Car starting with keyless entry...")


v = Vehicle()
v.start()

c = Car()
c.start()