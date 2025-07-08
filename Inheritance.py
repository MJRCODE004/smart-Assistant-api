
class Mammal:
 def walk(self)-> None:
     print(10)


class Dog(Mammal):
 def bark(self) -> None:
    print("Bark")

dog = Dog()
dog.walk()
dog.bark()