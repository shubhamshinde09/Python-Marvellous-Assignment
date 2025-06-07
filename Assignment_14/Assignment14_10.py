# 10 Access Modifiers Demonstration
class EmployeeAccess:
    def __init__(self, name, department, salary):
        self.name = name                  # public
        self._department = department     # protected
        self.__salary = salary            # private

    def show(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")


e1 = EmployeeAccess("Rahul", "IT", 70000)
e1.show()
print(e1.name)          # public access
print(e1._department)   # protected access (by convention)
print(e1._EmployeeAccess__salary)  # private access (name mangling)