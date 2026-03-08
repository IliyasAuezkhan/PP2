import os
import shutil

shutil.copy("demofile.txt", "bro.txt")
with open("bro.txt", "r") as f:
    print(f.read())
with open("ww.txt", "x") as f:
    pass
os.remove("ww.txt")