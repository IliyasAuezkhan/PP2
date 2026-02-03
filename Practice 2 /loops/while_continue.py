# 1 example

i = 0
while i < 6:
  i += 1
  if i == 3: # skip 3 dont print it
    continue
  print(i)
  
# 2 example 

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # work if and only if loop ended without any breaks
