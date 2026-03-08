with open("demofile.txt", "r") as f:
  print(f.read())
  print(f.readline())
  print(f.read(5))
  for x in f:
    print(x)
  print(f.readlines())