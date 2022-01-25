weather = "storm"

if weather == "raining":
    print("Take an umbrella.")
elif weather == "sunny":
    print("Wear Sunglasses")
elif weather == "dusty":
    print("Wear a mask")
elif weather == "cold":
    print("Wear A Jacket")
else:
    print("Unknown Weather.")

# comparision operator

'''
> - greater than
< - less than
== - equal to
<= - less than or equal to
>= - greater than or equal to
!= - not equal to
'''

score = int(input("Enter the score: "))

if score <= 100 and score >= 90:
    if score <=100 and score >= 95:
        print("A+")
    else:
        print("A")
elif score < 90 and score >= 80:
    if score < 90 and score >= 85:
        print("B+")
    else:
        print("B")
elif score < 80 and score >= 70:
    if score < 80 and score >= 75:
        print("C+")
    else:
        print("C")
elif score < 70 and score >= 60:
    if score < 70 and score >= 65:
        print("D+")
    else:
        print("D")
elif score < 60 and score >= 50:
    print("D-")
elif score < 50 and score >= 40:
    print("E")
elif score < 40 and score >=0:
    print("F")
else:
    print("Invalid Score")