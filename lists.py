names = ['David', 'John', 'Smith', 'Yusuf']

#                  0    1   2     3
student_info = ['David',12,True,'Dubai, UAE']

print(student_info[1])

# using a for loop to access all the items in the list

# traditional way

for itr in range(len(names)):
    print(names[itr])

# the fashionble way

def printList():
    print()

    for name in names:
        print(name)

# add an item in a list

# append() - adds a new list item in the end of the list

names.append('George')

printList()

# extend() - add more than one item in a list (the end of the list)

names.extend(['Rebbecca', 'Lisa'])

printList()

# insert() - add an item on a specified index number

names.insert(2, "Josh")

printList()


# remove items for a list

# remove() - this is used to remove a specified item from a list

names.remove('Smith')

printList()

# pop() - remove an item by specifying the index number

names.pop(4)

printList()

# copy of the list

copy_names = names.copy()

print(copy_names)

# NOTE: lists can accept dupliate values

# tuples

fruits = ('apples', 'bananas', 'oranges')

