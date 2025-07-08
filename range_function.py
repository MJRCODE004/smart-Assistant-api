# range() - function used to generate a sequence of numbers
numbers = range(5) # - setting up the ending range
for i in numbers:
    print(i)

print("-------------------------------")
numbers = range(1,10) # - setting up starting and ending index
for i in numbers:
    print(i)

print("-------------------------------")

numbers = range(1,50,10) # - Setting up the start , end and step up
for i in numbers:
    print(i)


print("------------------------------")
# By range() in for loop itself
for i in range(1,45):
    print("*")