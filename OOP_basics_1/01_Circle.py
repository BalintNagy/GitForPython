# Green Fox OOP Basics 1 - 1. feladat

# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area


import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return pow(self.radius, 2) * math.pi

karika = Circle(5)

print(karika.get_circumference())

print(karika.get_area())
