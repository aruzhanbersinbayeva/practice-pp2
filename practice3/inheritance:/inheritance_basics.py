class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

class Person:
    def walk(self):
        print("Walking...")

class Student(Person):
    pass

s = Student()
s.walk()  

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    pass

c = Car()
c.move()  