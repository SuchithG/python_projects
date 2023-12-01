f = open('sample.txt', 'a+') # append mode
print('Cursor at', f.tell())  # for append the cursor position is at the end 
print("Django is for web development\n") # new line being appended to an existing file
f.seek(0)
a = []
for line in f:
    a.append(line)
print(a)
f.close()