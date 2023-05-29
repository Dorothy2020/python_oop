class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f" I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.color} ")

class Dog(Pet):
   def speak(self):
       print("bark")


p = Pet("Tim",20)
p.speak()
c = Cat("Shrawdy",15,"brown")
c.speak()












