numbers = [3, 7, 12, 19]
print(list(filter(lambda x: x > 10, numbers)))


words = ["hi", "hello", "yes"]
print(list(filter(lambda w: len(w) >= 3, words)))


grades = [45, 80, 60, 30]
print(list(filter(lambda g: g >= 50, grades)))