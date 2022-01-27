# inheritance

# parent class
class Vehicle:
    def __init__(self, brand, wheels, seats):
        self.brand = brand
        self.wheels = wheels
        self.seats = seats

    def __str__(self):
        return f'''Brand: {self.brand}
Wheels: {self.wheels}
Seats: {self.seats}'''


# child class
class Car(Vehicle):
    def __init__(self, brand, wheels, seats, color):
        super().__init__(brand, wheels, seats)
        self.color = color

    def __str__(self):
        return f'''\nBrand: {self.brand}
Wheels: {self.wheels}
Seats: {self.seats}
Color: {self.color}'''

# child class
class Motorcycle(Vehicle):
    def __init__(self, brand, wheels, seats, noOfCylinders):
        super().__init__(brand, wheels, seats)

        self.noOfCylinders = noOfCylinders
    
    def __str__(self):
        return f'''\nBrand: {self.brand}
Wheels: {self.wheels}
Seats: {self.seats}
No Of Cylinders: {self.noOfCylinders}'''


vehicle1 = Vehicle("BMW", 4, 5)
print(vehicle1)

car_vehicle = Car("BMW", 4, 5, "Q-Ink")
print(car_vehicle)

motorcycle_vehicle = Motorcycle("Harley Davidson", 2, 2, 4)
print(motorcycle_vehicle)