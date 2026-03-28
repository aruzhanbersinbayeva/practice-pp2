#1
import re
s=r"ab*"
test=["ab","abb","abbb","a","b","ac","abc"]
for i in test:
    if re.fullmatch(s,i):
        print(f"'{s}' Matches")
    else:
        print(f"'{s}' Does not match")



#2
import re
s=r"ab[2-3]"
test=["ab2","ab3","ab1","ab4","ab","a","b"]
for i in test:
    if re.fullmathc(s,i):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")

#3
import re
test=["hello_world  my_Variable  abc_123  another_example"]
s=r"[a-z]+_ [a-z]+"
match=re.findall(s,test)
print(match)

#4
import re
s=r"[A-Z][a-z]+"
test=["Alice","Bob","Charlie","david","Eve"]
for i in test:
    if re.fullmatch(s,i):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does not match")


#5
import re
strings = ["ab", "acb", "a123b", "a--b", "abc", "b"]

pattern = r"^a.*b$"

for s in strings:
    if re.fullmatch(pattern, s):
        print(f"'{s}' matches")
    else:
        print(f"'{s}' does NOT match")


#6
import re
text = "Hello, world. This is a test."
new_text = re.sub(r"[ ,\.]", ":", text)
print(new_text)


#7
import re
snake_str = "my_variable_name"
matches = re.findall(r'_([a-z])', snake_str)  
print("Буквы после '_':", matches)
camel_str = snake_str  
for letter in matches:
    camel_str = camel_str.replace('_' + letter, letter.upper())
    print("После замены '_" + letter + "':", camel_str)

print("Snake case:", snake_str)
print("Camel case:", camel_str)

#8
import re

text = "HelloWorldPythonIsFun"
pattern = r'(?=[A-Z])'
words = re.split(pattern, text)
words = [w for w in words if w]
print("Original string:", text)
print("Split at uppercase letters:", words)


#9
import re
text = "HelloWorldPythonIsFun"
new_text = re.sub(r'(?=[A-Z])', ' ', text).strip()
print("Original string:", text)
print("With spaces inserted:", new_text)

#10
import re

camel_str = "myVariableName"
matches = re.findall(r'[A-Z]', camel_str)
print("Заглавные буквы:", matches)
snake_str = camel_str
for letter in matches:
    snake_str = snake_str.replace(letter, '_' + letter.lower())
    print(f"После замены '{letter}':", snake_str)

print("Camel case:", camel_str)
print("Snake case:", snake_str)