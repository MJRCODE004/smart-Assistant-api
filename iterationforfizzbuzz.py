def numbers():
    for x in range(1, 51):
        if x % 4 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 5 == 0:
            print("buzz")
        elif x % 4 == 0:
            print("fizzz")
        else:
            print(x)

numbers()

