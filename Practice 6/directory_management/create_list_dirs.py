import os
os.mkdir("Test.txt")
os.makedirs("Sasha/go/to")
print(os.listdir()) 
print(os.getcwd()) #current
files = os.listdir()
for file in files:
    if file.endwith(".txt"):
        print(file)