class Car:
    def __init__(self):
        pass
    def name(self,brand):
        self.brand = brand
        
    def display(self):
        print(f"i am using a formatted print statement for displaying this car name {self.brand}")
    def addType(self, type):
        self.type = type
        print("The type fo this car is ",self.type)