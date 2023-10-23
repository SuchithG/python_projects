from functools import reduce # module functools

lst = [5,10,15,20]

result = reduce(lambda x,y: x+y, lst)

print(result)