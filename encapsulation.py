# Method used to hide some features
# making our data private in python is by use of double underscore
# Encapsulation also checks the accessibility of variables

class Hello:
    def __init__(self ,name):
        self.a = 30
        self._b = 40
        self.__c = 50
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)


person = Person("Dory",23)
# access using class method

person.display()
# accessing directly from outside

hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)

