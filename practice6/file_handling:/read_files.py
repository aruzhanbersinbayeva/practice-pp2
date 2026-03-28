with open("example.txt", "r") as f:
    print(f.read())

# append
with open("example.txt", "a") as f:
    f.write("New line added\n")
    