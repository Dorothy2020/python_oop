# Method used to hide some features
# making our data private in python is by use of double underscore

class Hello:
    def __init__(self ,name):
        self.a = 30
        self._b = 40
        self.__c = 50


hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)

