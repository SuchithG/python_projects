lst = [10, 20, "Suchith", 40.2, -12] # Create a list and add elements to it
print(lst)
print(lst[2]) # Indexing
print(lst[3:5]) # Slicing
print(lst*2) # Repeating
print(len(lst)) # Length

# Dynamically adding or removing elements from a list\
lst.append(40) # adds elements to the list at the end 
lst.remove("Suchith")
del(lst[3]) # del function to remove elements using index
print(lst)

#lst.clear() # Remove all elements from list
#print(lst)

print(max(lst)) # print max element
print(min(lst)) # print min element

lst.insert(3, 99) # insert element at the index
print(lst)

lst.sort() # sort elements in ascending
lst.reverse() # reverse elements
print(lst)