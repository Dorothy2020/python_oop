# A python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name


# create a child Bus that will inherit  variables and methods of a parent class

class Bus(Vehicle):
    pass


# class inheritance

# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.


School_Bus = Bus("School Volvo", 200, 30)

print(" School name:", School_Bus.name, "speed:", School_Bus.max_speed, "mileage:", School_Bus.mileage)


#  Create  Animal class without any variables and methods

class Animal:
    pass  # it returns null






vehicle = Vehicle(200, 30,"Volvo")
print(vehicle.max_speed, vehicle.mileage)
