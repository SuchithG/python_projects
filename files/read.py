# read from an existing file
import os, sys

if os.path.isfile('myfile.txt'):
    f = open('myfile.txt', 'r')
else: 
    print("File Does not Exist")
    sys.exit(1)

s = f.read()
print(s)
f.close()