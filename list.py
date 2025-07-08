# LIST is also a object

# List Declaration
names = ['Monash','mano','kim']
print(names)

# To access element in the list by using the index value
names = ['Monash','mano','kim']
print(names[2])  # kim

# To access last element without knowing the index value
names = ['Monash','mano','kim']
print(names[-1]) # kim

# To add new value in the particular index
names [0] = 'Monesh'
print(names) # ['Monesh', 'mano', 'kim']

# python access in list
names = ['Monash','mano','kim','john','hema']
print(names[0:3]) #['Monash', 'mano', 'kim']  -- new list
# python takes from first index and not add the last index to get , instead of that it takes the last before index. It return the new list
print(names)


# List Methods

# Append() - is to add value in end of the list

numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(10) # - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# insert() - is used to add value in between the list
numbers = [1,2,3,4,5,6,7,8,9]
numbers.insert(2,14)
print(numbers) # - [1, 2, 14, 3, 4, 5, 6, 7, 8, 9]

# remove() - is used to remove particular value in the list
numbers  = [1, 2, 14, 3, 4, 5, 6, 7, 8, 9]
numbers.remove(14)
print(numbers) # - [1, 2, 3, 4, 5, 6, 7, 8, 9]

# clear() - is used to remove all items in the list does not ask any parameters
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.clear()
print(numbers) # - [] empty list

# Boolean expression to check items available in the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print( 3 in numbers) # - True

#len() - this function used to check the length of the list
print(len(numbers)) # - 9