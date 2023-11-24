f = open('sample.txt', 'r')

print(f.read())

f.seek(0) # file cursor to beginning or any position
print(f.readline())

f.seek(0)
print(f.readlines()) # returns the list of all the lines in the file from beginning along with the new line character
f.close()