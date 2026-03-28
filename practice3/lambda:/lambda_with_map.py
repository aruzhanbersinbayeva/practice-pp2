nums = [1, 2, 3, 4]
print(list(map(lambda x: x + 10, nums)))

temps = [0, 10, 20]
print(list(map(lambda t: t * 9/5 + 32, temps))) 


words = ["python", "code"]
print(list(map(lambda w: w.capitalize(), words)))