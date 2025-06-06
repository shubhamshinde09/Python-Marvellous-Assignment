class Demo:
    Value = 0 # Class variable 

    def __init__(self,no1, no2):
        self.no1 = no1
        self.no2 = no2
#instance mathod fun 
    def Fun(self):
        print(f"Fun Method - no1: {self.no1},no2: {self.no2}")        
    
#instance mathod gun 
    def Gun(self):
        print(f"Gun Method - no1: {self.no1},no2: {self.no2}")    

#creating obj 
obj1 = Demo(11,21)
obj2 = Demo (51,101)       

# calling instance methodes
obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()

