student_info = {
    "student_id" : 1345,
    "name" : "Josh Killa",
    "dateOfBirth" : "25 Sept 2005"
}

# access a value by specifying the key

print(student_info["name"])

# access all the items in a dictionary (i.e. the key and values)

for student_keys, student_values in student_info.items():
    print(f"{student_keys:25} {student_values}")

# access the keys only in a dictionary

for student_keys in student_info.keys():
    print(student_keys)

# access the values only in a dictionary

for student_values in student_info.values():
    print(student_values)

# add an item in a dictionary

student_info["address"] = "Dubai, UAE"

for student_keys, student_values in student_info.items():
    print(f"{student_keys:25} {student_values}")

# update an item in a dictionary

student_info['dateOfBirth'] = "16 Aug 2006"

for student_keys, student_values in student_info.items():
    print(f"{student_keys:25} {student_values}")

print()

# remove items from a dictionary

# pop() - remove an itme from a ditionary by using the key

student_info.pop('address')

for student_keys, student_values in student_info.items():
    print(f"{student_keys:25} {student_values}")

# popItem() - remove the last item in the dictionary

print()

student_info.popitem()

for student_keys, student_values in student_info.items():
    print(f"{student_keys:25} {student_values}")

# example of using lists as values in a dictionary

cars_stock = {
    "Nissan" : ['Pathfinder', 'Altima', '370Z', 'Sentra', 'Patrol'],
    "Honda" : ['Civic', 'Accord', 'CR-V']
}

customer_brand = input("Enter the car brand you are looing for: ")

if customer_brand in cars_stock.keys():
    print("It's Available")
else:
    print("Not Available")

print()

for car_brand, car_model in cars_stock.items():
    print(car_brand)

    for model in car_model:
        print(model)
    
    print()