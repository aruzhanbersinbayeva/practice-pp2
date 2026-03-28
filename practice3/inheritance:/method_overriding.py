# Example 1
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark!")

Dog().speak()


# Example 2
class Person:
    def role(self):
        print("Human")

class Teacher(Person):
    def role(self):
        print("Teacher")

Teacher().role()


# Example 3
class Shape:
    def area(self):
        print("Unknown area")

class Square(Shape):
    def area(self):
        print("Area = side * side")

Square().area()