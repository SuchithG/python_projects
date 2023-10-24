def square(fun):
    def inner():
        n = fun()
        return n*n
    return inner

def half(fun):
    def inner():
        n = fun()
        return n/2
    return inner

@square # decorate a function named first with another function name second 
@half
def num():
    return 10

result = num()
print(result)