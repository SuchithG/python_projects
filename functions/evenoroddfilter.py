# using filter retrieve only even numbers from a given list

lst = [10,2,43,78,12,9]

result = list(filter(lambda x: x%2 == 0, lst))

print(result)

for i in result: print(i)