# local and global variables
# accessing global variables with the same name

x = 123

def display():
    y = 678
    print(y)
    print(globals()['x']) 

print(x)
z = display # Assigns a function to a variable and invoking it 
z()