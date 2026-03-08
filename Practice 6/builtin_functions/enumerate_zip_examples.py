x = ["apple", "bro", "pp2"]
res = enumerate(x)
for number, value in res:
    print(number, value, sep = ":")
a = ["bro", "you", "dude"]
b = [99, 100, 32]
res = dict(zip(a, b))
for key, value in res.items():
    print(key, value, sep = ":")
s = "bro"
print(res[s])