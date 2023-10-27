from random import *

for i in range(10): # for range 10 random numbers
    print(random()) # will return a random floating point number between 0 and 1

for i in range(10): # for range 10 random numbers
    print(randint(1,50)) # random numbers between 1 to 50

for i in range(10): # for range 10 random numbers
    print(uniform(1,50)) # floating point random numbers, will not include first and last digits in the range

for i in range(10): # for range 10 random numbers
    print(randrange(1,12,2)) # start , stop and step

# dynamically define a list , and pick random numbers from it

list = ["java", "python", "C++", "Devops", "aws"]
for i in range(10):
    print(choice(list)) # passing a sequence using choice function