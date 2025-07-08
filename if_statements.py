# If Statements

temperature = input("Enter the temperature: ")

if  int(temperature) < 40: 
    print("Its cold")
elif int(temperature) == 40 :
    print("Its normal ")
elif int(temperature) > 40:
    print("Its Hot")
else:
    print("Its very Hot")