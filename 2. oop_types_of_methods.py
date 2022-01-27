# types of methods

# instance method - any method that has 'self' as the first argument
# class method - any method that has 'cls' as the first argument. @classmethod -> decorator
# static method - does not take any "first arguments"

class Cab:

    numberOfRunningCabs = 0
    numberOfPassengers = 0

    # constructor

    def __init__(self, driver, kms, places, pay, noOfPassengers):
        self.driver = driver
        self.kms = int(kms)
        self.places = places
        self.pay = int(pay)
        self.noOfPassengers = int(noOfPassengers)
        Cab.numberOfRunningCabs += 1
        Cab.numberOfPassengers += noOfPassengers

    # instance method

    def ratePerKm(self):
        return(round(float(self.pay/self.kms),2))

    # class method

    @classmethod
    def avgPassengers(cls):
        return cls.numberOfPassengers/cls.numberOfRunningCabs

    # static method
    def validatePay(pay):
        return pay > 0

firstCab = Cab("Deacon", 150, ['Dubai', 'Sharjah'], 300, 3)
seconCab = Cab("Sara", 50, ['Abu Dhabi', 'Sharjah'], 212, 2)

print(firstCab.places)

print(Cab.numberOfPassengers)
print(Cab.numberOfRunningCabs)

print(firstCab.ratePerKm())

print(Cab.avgPassengers())

print(Cab.validatePay(firstCab.pay))