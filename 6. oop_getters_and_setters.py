# getters and setters

class Uber:
    def __init__(self, driver, car_number):
        self.driver = driver
        self.car_number = car_number

    @property
    def uber_email(self):
        return f"{(self.driver).lower()}.{self.car_number}@uber.com"

uber_1 = Uber("Sara", 12536)

print(uber_1.driver)
print(uber_1.uber_email)

uber_1.driver = "Josh"

print(uber_1.driver)
print(uber_1.uber_email)
