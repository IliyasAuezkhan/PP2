# 1 example

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 2 example

numbers = [1, 2, -3, 4, -5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x > 0, numbers))
print(odd_numbers)

# 3 example

def isprime(a):
    if a == 0 or a == 1:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: isprime(x), numbers))
print(odd_numbers)

# 4 example

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 1, numbers))
print(odd_numbers)
