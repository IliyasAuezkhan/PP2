# 1 example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": #skip banana
    continue
  print(x)

# 2 example

for x in range(6):
  print(x) # 1,2,3,4,5
  
# 3 example

for x in range(2, 6):
  print(x) #2,3,4,5
  
# 4 example

for x in range(2, 6, 2): # third is increament
  print(x)
  
# 5 example

for x in range(2, 30, 3):
  print(x)
  
# 6 example

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# 7 example

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #will not print
  
# 8 example

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #nested loop like 2d dimensional array
    
# 9 example

for x in [0, 1, 2]:
  pass