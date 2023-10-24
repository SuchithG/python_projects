# create a generator
# keywords is used for creating custom generators - yield
def customgen(x,y):
    while x<y:
        yield x # will stack each value of x and store it in memory
        x+=1

result = customgen(20,30)

for i in result:
    print(i)