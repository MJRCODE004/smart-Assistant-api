name = input("Enter your name: ")
age = int(input("Enter your age: "))
id_status = input("Do you have an ID? (yes/no): ")


def enter_club(name: str, age: int, has_id: bool) -> str:
    if name.lower() == 'bob':
        return "Get out of the club, we don't want any trouble"

    if age >= 18 and has_id:
 
        return f"Welcome to the club, {name}!"
    else:
        return "You can't enter the club."

has_id = id_status.lower() == 'yes'

if __name__ == '__main__':
    result = enter_club(name, age, has_id)
    print(result)