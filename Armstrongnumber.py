given_number = 153

new_number = str(given_number)


sum = 0
for x in new_number:
    sum+= int(x)**3

if(sum == int(given_number)):
    print("The number is armstrong")
else:
    print("It is not Palindrome")