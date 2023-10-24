# Using the map function double the value of each element in the list
# applies a function/lambda on every element of the list and gives us a new list

lst = [1,2,3,4,5,6,7,8,9,10]

result = list(map(lambda n : n*2, lst))

print(result)