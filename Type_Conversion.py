# We can't subtract a integer to a string it shows error
 # Error_name  : unsupported operand type(s) for -: 'int' and 'str'
from variable import first_name

# Example Program

birth_year = input("Enter your Birth Year: ")
age = 2025 - (birth_year)
print(age)

# To overcome this error convert the str to integer to perform the action by using
#            int(birth_year) - This is called Type Conversion

                          # Solved program

birth_year = input("Enter your Birth Year: ")
age = 2025 - int(birth_year) # here the string is converted to integer
print(age) # 23

# There are Function which we can perform type conversion

#  1. int()     - to convert to Integer
#  2. float()   - to convert to float
#  3. bool()    - to convert to boolean
#  4. str()     - to convert to String


