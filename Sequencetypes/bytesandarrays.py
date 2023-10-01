lst = [20, 30, 40, 50, 60, 70, 80]
print(type(lst))
b = bytes(lst)
print(type(b))
#b[3] = 22 # element cannot be added 

b1 = bytearray(lst)
print(type(b1))
b1[3] = 22 # Indexing can be performed and we can add values to it
# print(b1*2) no repetitions