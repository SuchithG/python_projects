s = {23, 56, -79, "OK", "OK"} # does not consider duplicate values
print(s)

s.update([88,99]) # does not update values in particular order
print(s)

# print(s*2) # does not allow repeating 

s.remove(-79) # removes
print(s)

f = frozenset(s)
f.update([20])



