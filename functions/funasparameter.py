# Passing one function as a parameter to another

def display(fun):
    return "Hello "+ fun 

def name():
    return "Suchith"

print(display(name()))