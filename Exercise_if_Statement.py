weight = int(input("weight : "))
process = input("(k)g or (L) bs : ")

# pounds = kilograms * 2.20462
if process.upper() == "k":
    converted = weight / 0.45
    print("Weight in Lbs : " + str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs: " + str(converted))
