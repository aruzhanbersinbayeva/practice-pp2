import re
a=input()
b=re.findall(r"\d{2}/\d{2}/\d{4}",a)
print(len(b))