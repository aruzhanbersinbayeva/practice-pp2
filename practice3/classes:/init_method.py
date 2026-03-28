class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Aruzhan", 9)
print(s.name, s.grade)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Laptop", 1000)
print(p.price)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r = Rectangle(5, 3)
print(r.width * r.height)