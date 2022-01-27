def printFact():
    print("The chef's hat has excatly 100 pleats")

printFact()

# function with parameters

def customer_details(name, yearOfBirth, address):
    print(f'''Name: {name}
Year Of Birth: {yearOfBirth}
Address: {address}''')

customer_details('John', 2005, "Dubai, UAE")

# return in function

def login(username, password):
    if username == "john.doe@gmail.com" and password == "12345@":
        return True
    else:
        return False

isCustomer = login("john.doe@gmail.com", "12345@")

print(isCustomer)