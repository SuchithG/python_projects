tpl = (20, 56, 78, -85, "yes") # create a tuple 
# tpl1 = (20,) # Tuple or list with one element should always end with comma
print(type(tpl))

print(tpl*2)
print(tpl.count("yes"))
print(tpl.index(78))

print(tpl[:-1]) # Slicing 