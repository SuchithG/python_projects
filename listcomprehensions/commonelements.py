# Find the common elements of two lists

a = [1,4,6,8]
b = [1,2,3,4]
result = []

for i in a:
    if i in b:
        result.append(i)
print(result)