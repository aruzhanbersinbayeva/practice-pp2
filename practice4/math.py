import math
import random

print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Pi value:", math.pi)
print("Ceil 4.3:", math.ceil(4.3))
print("Floor 4.7:", math.floor(4.7))

print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
numbers = [1, 2, 3, 4, 5]
print("Random choice from list:", random.choice(numbers))
random.shuffle(numbers)
print("Shuffled list:", numbers)