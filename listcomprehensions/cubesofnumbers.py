""" 
lst = [] # list the cube of numbers defined in the range
for x in range(1,11):
    lst.append(x**3)
print(lst)
"""

# List comprehension

lst = []
lst = [x**3 for x in range(1,11)]
print(lst)