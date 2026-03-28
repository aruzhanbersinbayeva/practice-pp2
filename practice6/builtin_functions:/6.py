lines = ["Line1\n", "Line2\n"]

with open("example.txt", "w") as f:
    f.write("Hello\n")         # записали одну строку
    f.writelines(lines)        # добавили список строк