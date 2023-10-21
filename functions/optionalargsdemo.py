# variable args and optional arguments

def myfun(x, *args, **kwargs):
    print(x)
    print(args)
    for key, value in kwargs.items():
        print(key, value)

myfun(10,20,30,40,50, name="Suchith", sal="10000000")