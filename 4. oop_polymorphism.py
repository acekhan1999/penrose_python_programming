# polymorphism

# method overriding - ability to have the same method name in the parent and the child class

class Vehicle:
    def __init__(self,brand, wheels, seats):
        self.brand = brand
        self.wheels = wheels
        self.seats = seats

    def automobile(self):
        print("this is the parent automobile")

class Car(Vehicle):
    def __init__(self, brand, wheels, seats, noOfPassengers):
        super().__init__(brand, wheels, seats)
        self.noOfPassengers = noOfPassengers

    def automobile(self):
        print("this is the child automobile")

parent_obj = Vehicle("Tesla", 4, 5)
parent_obj.automobile()

child_obj = Car("Mazda", 4, 5, 5)
child_obj.automobile()

# method overloading - ability to create a method with flexibility.

class Football:

    def team_details(self, team = None):
        if team == None:
            print("No Team Specified")
        else:
            print(f"{team} is a wonderful team.")

real_madrid = Football()

real_madrid.team_details()
real_madrid.team_details('Real Madrid')

