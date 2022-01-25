name = "David Letterman"

print(f'''Our guest for today is
{name}!''')

# string indexes

#            012345678
city_name = "Abu Dhabi"

print(city_name[2])
print(city_name[3])

# string methods

# strip() - this function is responsible to get rid of any additional spaces before and after the string.
address = "      Dubai, UAE   ".strip()

print(f"The user lives in {address}.")

# len() - this function returns the length of a string (how many characters are there in a string)
print(len(address))

# upper() - this function changes all characters to uppercase
print(address.upper()) 

# lower() - this function changes all characters to lowercase
print(address.lower()) 

# title() - this function changes all characters to titlecase
print(address.title()) 

# split() - this is responsible to split data based on an indicator

fullname = "David Letterman"
print(fullname.split(" "))
firstname, lastname = fullname.split(" ")

print(f"Firstname: {firstname}")
print(f"Lastname: {lastname}")

# replace() - replaces a part of a string

new_address = "Dubai, UAE"
print(new_address)

new_address = new_address.replace("Dubai", "Abu Dhabi")
print(new_address)