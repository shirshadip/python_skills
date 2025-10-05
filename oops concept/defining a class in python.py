class car:
    #attribute (a variable inside a class)
    wheels = 4 #class object is same for all attributes

    #constructor, a special method 

    def __init__(self,brand,model) -> None:
        self.brand = brand #instance attribute 
        self.model = model #instance attribute

    #method ( a funtion inside a class)
    def showdetails(self):
        print(f"brand {self.brand },Model: {self.model},wheels:{self.wheels}")


car1 = car("toyota","corolla")
car2 =car("tesla", "model s ")


car1.showdetails()
car2.showdetails()#that runs when an object is created