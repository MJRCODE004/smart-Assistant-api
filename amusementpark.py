from envs.myenv.Lib.unittest.test.test_setups import resultFactory

name = input("Enter the name : ")
n = name.upper()
age = int(input("Enter the age : "))
id_avaiable = input(("Enter id if  (yes/no) :"))


def entry_func(str:name,int : age, bool : id_avaiable) -> str:
    if id_avaiable.upper() == "yes":
        print( "You are eligible to enter the amusement park")

    if age >=18 and id_avaiable:
        print(f"Welcome to the Park ,{name} ! ")

    elif id_avaiable == "yes" :
        print("welcome")
    else:
        print("Don't enter the park")


if __name__ == '__main__':
    result = entry_func(str,int,bool)