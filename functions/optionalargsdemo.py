# variable args and optional arguments

def myfun(x, *args, **kwargs):
    print(x)
    for each_args in args:
        print(each_args)
    for each_kw in kwargs:
        print(each_kw)

myfun(10,20,30,40,50, name="Suchith", sal="10000000")