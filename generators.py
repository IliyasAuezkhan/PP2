# 1 example

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# 2 example

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 3 example

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# 4 example

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 5 example

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# 6 example

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# 7 example

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# 8 example

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

# 9 example

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# 10 example

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

# 11 example

bro = [x * x for x in range(5)]
print(bro) # 0 1 4 9 16

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

# 12 example

total = sum(x * x for x in range(10))
print(total)

# 13 example

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

# 14 example

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# 15 example

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# 16 example

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally: # work when try end or error or we use close method
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

# Exercises

# 1

def squares_upto_n(n):
    for i in range(n + 1):
        yield i * i

for value in squares_upto_n(5):
    print(value)

# 2

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


n = int(input())

print(",".join(str(num) for num in even_numbers(n)))

# 3

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_and_4(50):
    print(num)

# 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for value in squares(3, 7):
    print(value)

# 5

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
