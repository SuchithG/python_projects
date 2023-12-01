f = open('sample.txt', 'r') # read mode

print(len(f.readlines()))

print(len(f.read().split('\n')))