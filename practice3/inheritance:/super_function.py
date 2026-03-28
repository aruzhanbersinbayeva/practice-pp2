# Example 1
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Bulldog")
print(d.name, d.breed)


# Example 2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ali", 9)
print(s.name, s.grade)


# Example 3
class Vehicle:
    def __init__(self, type_):
        self.type_ = type_

class Car(Vehicle):
    def __init__(self, type_, color):
        super().__init__(type_)
        self.color = color

c = Car("Sedan", "Red")
print(c.type_, c.color)