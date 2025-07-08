# Strings in python are objects

print('Strings in python are objects')


course = " Python for Beginners"

# upper() -  used to change the Entire String into uppercase
#  this upper() function does not cha ge our original String it return a new String
print(course.upper()) # PYTHON FOR BEGINNERS


# lower() - used to change the Entire String into lowercase
# this lower() function does not change our original String it return a new String
print(course.lower()) # python for beginners

# find() - is used to get the index of that particular Character
print(course.find('P')) # 1
# Here the index value for the character y is 1

# replace() = is used to replace the string with updated string
# function does not change our original String it return a new String
print(course.replace("Beginners","Everybody"))  # Python for Everybody

# To check particular string in the String we can use in
print("for" in course) # True

print(course) #  Python for Beginners


