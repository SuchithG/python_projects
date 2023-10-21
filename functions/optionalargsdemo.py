# variable args and optional arguments

def myfun(x, *args):
    print(x)
    print(args)

myfun(10,20,30,40,50)