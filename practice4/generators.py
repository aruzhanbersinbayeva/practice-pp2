class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("Iterator example:")
for num in CountDown(5):
    print(num)

def even_numbers(limit):
    for n in range(limit + 1):
        if n % 2 == 0:
            yield n

print("\nGenerator example:")
for even in even_numbers(10):
    print(even)