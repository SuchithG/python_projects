f = open('sample.txt', 'r')

print(f.read())

f.seek(0)
print(f.readline())