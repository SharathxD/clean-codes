class Car:
    def __init__(self):
        pass
    def name(self,brand):
        self.brand = brand
        
    def display(self):
        print(f"i am using a formatted print statement for displaying this car name {self.brand}")