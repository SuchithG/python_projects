# function to calculate the average of two numbers 

def average(a, b):
    print(a)
    print(b)
    #print("Average of two numbers is",(a+b)/2)
    return (a+b)/2


print(average(b=10, a=20)) # passing keyword argument

# default arguments

def avg(a=2,b=3):
    return (a-b)/2

print(avg())