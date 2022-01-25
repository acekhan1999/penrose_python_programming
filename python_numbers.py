import math

num1 = 5
num2 = 3

# arithematic operations

sum = num1+num2
difference = num1-num2
product = num1*num2
quotient = num1/num2
remainder = num1%num2
exponent = num1**num2

print(f'''
Sum: {sum}
Difference: {difference}
Product: {product}
quotient: {quotient}
remainder: {remainder}
exponent: {exponent}'''.title())

# mathematical function provided by python

# round() - round off a number
random_num = 1.77890

print(round(random_num))

# rounding off to the nearest two decimal places
print(round(random_num, 2))

# math.ceil() - highest possible value

random_num = 1.223
print(math.ceil(random_num))

# math.floor() - lowest possible value

random_num = 1.889
print(math.floor(random_num))

# math.sqrt() - returns the square root of a number

print(math.sqrt(25))