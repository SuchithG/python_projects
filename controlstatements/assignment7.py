# Enter a number and determine wether it is prime or not.
#uses a flag variable to keep track of whether the number is prime and a while loop to check for divisibility by all numbers from 2 up to num - 1. If any of these divisions result in a remainder of 0, the flag is set to False, indicating that the number is not prime. Otherwise, if no divisions result in a remainder of 0, the flag remains True, indicating that the number is prime.

flag = True
i = 2
num = int(input("Enter a number: "))

while i < num:
    if (num % i) == 0:
        flag = False
    i = i + 1

if flag:
    print('Number is a Prime Number')
else:
    print('Number is not a Prime Number')