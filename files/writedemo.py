f = open('sample.txt', 'w+')

f.write("Python is awesome\n")
f.writelines(["Python\n","Django\n","DRF\n"]) # writes a list in new line in list
f.seek(0) # cursor will move to the beginning of the file
print(f.read())  # Read the contents of the file