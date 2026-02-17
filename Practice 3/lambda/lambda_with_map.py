# 1 example

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 2 example

bro = [1, -8, 6, 9]
res = list(map(lambda x : abs(x), bro))
print(res)

# 3 example

bro = [1, 8, 6, 9]
res = list(map(lambda x : x + 100, bro))
print(res)

# 4 example

bro = [1, 8, 6, 9]
res = list(map(lambda x : x ** x, bro))
print(res)