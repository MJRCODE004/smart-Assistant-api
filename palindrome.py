given_string ="madam"

new_string = ""

for x in given_string:
    new_string = x+new_string
print(new_string)

if(given_string == new_string):
    print("The string is Palindrome")
else:
    print("it is not Palindrome")

"____________________________________________________"

gs = input("Enter the string to check : ")

ns = ''

for x in gs:
    ns = x+ns


if(ns==gs):
    print("It is Palindrome")
else:
    print("it is not palindrome")

