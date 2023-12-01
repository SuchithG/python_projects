f = open('sample.txt', 'w+')

f.write("Python is awesome\n")
f.writelines(["Python\n","Django\n","DRF\n"]) # writes a list in new line in list
print('Cursor is at ', f.tell())
f.seek(0) # cursor will move to the beginning of the file
print('Cursor is at ', f.tell())
print(f.read())  # Read the contents of the file
f.close()