# class 

class Employee:

    # class properties
    required_document = "passport"
    noOfEmployees = 10
    
    # constructor

    def __init__(self, name, age, position, yearOfJoin):
        self.name = name
        self.age = int(age)
        self.position = position
        self.yearOfJoin = int(yearOfJoin)
        Employee.noOfEmployees -= 1

# creating an Employee object
print(Employee.noOfEmployees)

deacon = Employee("Deacon St. John", 34, "Sales Rep.", 1996)

print(deacon.position)

print(deacon.required_document)

print(Employee.noOfEmployees)