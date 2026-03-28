i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue 
    print(i)  



while True:
    text = input("Type something (or 'skip' to skip, 'exit' to stop): ")
    if text == "exit":
        print("Loop stopped")
        break
    if text == "skip":
        continue  
    print("You typed:", text)



number = 0
while number < 10:
    number += 1
    if number == 5:
        continue 
    print("Number is:", number)