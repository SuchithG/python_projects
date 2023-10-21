# variable args and optional arguments

def myfun(x, *pos_param, **key_param):
    print(x)
    print(pos_param)
    for key, value in key_param.items():
        print(key, value)

myfun(10,20,30,40,50, name="Suchith", sal="10000000")