lst = [10, 20, "Suchith", 40.2, -12] # Create a list and add elements to it
print(lst)
print(lst[2]) # Indexing
print(lst[3:5]) # Slicing
print(lst*2) # Repeating
print(len(lst)) # Length

# Dynamically adding or removing elements from a list\
lst.append(40)
lst.remove("Suchith")
print(lst)