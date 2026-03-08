with open("demofile.txt", "w") as f:
  f.write("Opps\n")
with open("demofile.txt", "a") as f:
  f.write("We will fix it")
with open("bro.txt", "x") as f:
  pass