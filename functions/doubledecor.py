# create a decorator function that will return double the number returned ny that function

def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

def num():
    return 5

resultfun = decor(num)
print(resultfun())