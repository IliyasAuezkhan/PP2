# 1 example

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x) # 5

# 2 example

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x) # 5
del p1
print(p1.x) # not defined

# 3 example

class MyClass:
  x = 5
  y = 6
  z = 7

p1 = MyClass()
print(p1.x) # 5
print(p1.y)
print(p1.z)

# 4 example

class Person:
    pass