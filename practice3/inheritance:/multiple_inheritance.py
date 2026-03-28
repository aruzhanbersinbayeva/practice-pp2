# Example 1
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

child = Child()
child.skills()  


# Example 2
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

C().greet()  


# Example 3
class X:
    def x(self):
        print("X method")

class Y:
    def y(self):
        print("Y method")

class Z(X, Y):
    pass

z = Z()
z.x()
z.y()