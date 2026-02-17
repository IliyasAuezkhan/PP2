# 1 example

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
#2 example

def get_greeting():
  return "Hello from a function"

print(get_greeting())

# 2 example

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") # order matter

# 3 example

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

# 4 example

def my_function(name, /): # only positional
  print("Hello", name)

my_function("Emil")

def my_function(*, name): # only keyword
  print("Hello", name)

my_function(name = "Emil") 

def my_function(a, b, /, *, c, d): #Arguments before / are positional-only, and arguments after * are keyword-only:
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)