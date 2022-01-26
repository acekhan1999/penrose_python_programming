
while True:
    try:
        age = int(input("Enter your age: "))

    except:
        print("Please enter you age in an integer format.")

    else:
        print(age)
        break


while True:
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))

    except ValueError:
        print("Please enter number in ints")

    else:

        try:
            result = dividend/divisor

        except ZeroDivisionError:
            print("Division by zero is not possible!")
        
        else:
            print(result)
            break