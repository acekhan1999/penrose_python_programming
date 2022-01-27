# encapsulation


class RealEstate:
    def __init__(self):
        # public properties

        self.type = "Luxury"
        self.sqft = 2100
        self.price = 1000000
        self.address = "Dubai, UAE"

        # private properties

        self.__owner_name = "Deacon St. John"
        self.__owner_address = "Dubai, UAE"
        self.__owner_email = "deacon.john@gmail.com"

    def owner_info(self):
        print(f'''Owner Name: {self.__owner_name}
Owner Address: {self.__owner_address}
Owner Email: {self.__owner_email}''')

class Owner(RealEstate):
    def __init__(self):
        super().__init__()

    def owner_info(self):
        return super().__owner_info()


cust1 = RealEstate()
# print(cust1.__owner_name)

cust1.owner_info()

owner1 = Owner()
owner1.owner_info()