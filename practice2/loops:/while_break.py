i = 1
while i <= 10:
    print(i)
    if i == 5:  # досрочно останавливаем цикл
        print("Breaking the loop!")
        break
    i += 1


while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        print("Loop stopped by user")
        break
    print("You typed:", text)


number = 0
while number < 20:
    if number % 7 == 0 and number != 0:
        print("Found a multiple of 7:", number)
        break
    number += 1