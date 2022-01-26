# a for loop is a loop tha runs on a specified range

for itr in range(5):
    print(itr, "Hello World")

# for loop to access all the characters in the string

name = "Yusuf"

for itr in range(len(name)):
    print(name[itr].upper())

print()

for character in name:
    print(character.upper())

print()

# break - it is used to break the loop before full execution

for a in range(15):
    print("Mark")

    if a == 5:
        print("the loop was broken")
        break

# example 1 - finding vowels in a word

word = "table"

vowels = 'aeiou'

vowels_in_word = ''

for letter in word:
    if letter in vowels:
        vowels_in_word += letter

print(vowels_in_word)