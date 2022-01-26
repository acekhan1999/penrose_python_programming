import random

# conditional loop

password = '12345@'

pin = input("Enter the password: ")

while password != pin:
    pin = input("Invalid Password. Enter the password again: ")

print("Welcome to your account.")

counter = 0

while True:
    counter +=1 
    print(counter)

    if counter == 25:
        break

counter = 0

while True:
    dice = random.randint(1,6)

    if dice != 6:
        counter += 1
        continue
    else:
        break

print(f"it took {counter} tries to get a 6")