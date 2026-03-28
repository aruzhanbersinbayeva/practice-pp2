def multiply_all(*numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

print(multiply_all(2, 3, 4))


def show_student(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_student(name="Aru", grade=9, city="Almaty")


def mix(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

mix(1, 2, name="Ali", age=17)