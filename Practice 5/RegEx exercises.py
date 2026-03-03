# 1

import re
a = str(input())
x = re.findall("ab*", a)
print(x)

# 2

import re
a = input()
x = re.findall(r"ab{2, 3}", a)
print(x)

# 3

import re
a = input()
x = re.findall(r"[a-z]+_[a-z]+", a)
print(x)

# 4

import re
a = input()
x = re.findall(r"[A-Z][a-z]+", a)
print(x)

# 5

import re
a = input()
x = re.findall(r"a.*b", a) # ? first occurance 
print(x)

# 6

import re
a = input()
x = re.sub(r"[ ,.]", ":", a)
print(x)

# 7 

import re
a = input()
x = re.split("_", a)
camel = x[0]
for word in x[1:]:
    camel += word.capitalize()

print(camel)

# 8

import re 
a = input()
x = re.split(r"([A-Z][a-z]*)", a)
x = [word for word in x if word != ""]
print(x)

# 9

import re
a = input()
x = re.sub(r"([A-Z])", r" \1", a).strip()
print(x)

# 10

import re
camel = input()
x = re.split(r"([A-Z][a-z]*)", camel)
res = ""
res = x[0]
for word in x[1:]:
    if word:
        res += "_" + word.lower()

print(res)