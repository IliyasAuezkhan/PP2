# 1 example

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
 
# 2 example

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# 3 example

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") # order matter

# 4 example

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

# 5 example

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# 6 example

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# 7 example

def my_function(name, /): # only positional
  print("Hello", name)

my_function("Emil")

# 8 example

def my_function(*, name): # only keyword
  print("Hello", name)

my_function(name = "Emil") 

# 9 example

def my_function(a, b, /, *, c, d): #Arguments before / are positional-only, and arguments after * are keyword-only:
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

# 10 example

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# 11 example

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

