# Enter a number and determine wether it is prime or not.

num = input("Enter a number: ")
if num.isnumeric():
    num = int(num)
    primeFlag = True

    if num <= 1:
        primeFlag = False
    else:
        for i in range(2, num):
            if num % i == 0:
                primeFlag = False
                break

    if primeFlag:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print("Invalid input. Please enter a valid number.")