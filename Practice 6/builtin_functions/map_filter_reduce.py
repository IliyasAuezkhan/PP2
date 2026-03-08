from functools import reduce
a = [1, 2, 3, 4, 5, 6]
def square(b):
    return b * b
def even(b):
    if b % 2 == 0:
        return True
    return False
mapres = list(map(square, a))
print(*mapres)
filterres = list(filter(even, a))
print(*filterres)

reduceres = reduce(lambda x, y: x * y, a)
print(reduceres)
reduceres2 = reduce(lambda x, y: x if x > y else y, a) #max
print(reduceres2)