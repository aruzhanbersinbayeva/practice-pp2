for i in range(1, 11):
    print(i)
    if i == 5: 
        print("Breaking the loop!")
        break


fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        print("Found cherry, stopping loop")
        break
    print(fruit)


for number in range(10):
    if number % 7 == 0 and number != 0:
        print("Found a multiple of 7:", number)
        break