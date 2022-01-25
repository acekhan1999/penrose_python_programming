# input() - this function is used to take information from the user.

name = input('Enter your name: ')
print(name)

# int() - this function is used to convert a string to an int

age = int(input("Enter the age: "))
# print(type(age))
print(age)

# float() - this function will convert the string to a float

account_balance = float(input("Enter your account balance: "))
print(type(account_balance))
print(account_balance)

# print() - prints the data of the variable and also print the statement

# print("The new customer's name is",name,"He is",age,"years old. And his account balance is:",account_balance)

# f string formatting

print(f"The new customer's name is {name}. He is {age} years old. And his account balance is {account_balance:,}")