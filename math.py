# 1 example

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# 2 example

x = abs(-7.25)

print(x)

# 3 example

x = pow(4, 3)

print(x)

# 4 example

import math

x = math.sqrt(64)

print(x)

# 5 example

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# 6 example

import math

x = math.pi

print(x)


# Exercises

# 1

import math
a = int(input())
b = math.radians(a)
print(b)

# 2 

a = float(input())
b = float(input())
c = float(input())
print(a * (b + c) / 2)

# 3 

import math
n = float(input())
l = float(input())
print(n * l * l / (4 * math.tan(math.pi / n)))

# 4

a = float(input())
h = float(input())
print(a * h)