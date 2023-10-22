# variable args and optional arguments

def myfun(x, *pos_param, **key_param):
    print(x)
    key_param['id'] = 123
    print(pos_param)
    for key, value in key_param.items():
        print(key, value)
    modified_pos_param = pos_param+(50,)
    myfun2(*modified_pos_param, **key_param)
    

def myfun2(*args, **kwargs):
    print(args)
    print(kwargs)

myfun(10,20,30,40,50, name="Suchith", sal="10000000")