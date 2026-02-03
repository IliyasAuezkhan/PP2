# 1 example


a = 5
b = 2
if a > b: print("a greater than b")

# 2 example

a = 1
b = 1000000
print("A") if a > b else print("B")

# 3 example

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# 4 example

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# 2 elif

# 5 example

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

# 6 example

username = "" # return false
display_name = username if username else "Guest"
print("Welcome,", display_name)

# 7 example

a = 200
b = 33
c = 500
if a > b and c > a: #& like in c++
  print("Both conditions are True")

# 8 example

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
# 9 example

a = 33
b = 200
if not a > b: # reverse the result of the conditional statement
  print("a is NOT greater than b")
  
# 10 example

#priority 1) not 2) and 3) or  
# if (((age < 18 or age > 65) and (not is_student)) or has_discount_code):
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
  
# 11 example

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")
  
# 12 example

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")
  
# 13 example

score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")
  



