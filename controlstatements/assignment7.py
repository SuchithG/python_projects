# Enter a number and determine wether it is prime or not.

num = input("Enter a number: ")
if num.isnumeric():
    num = int(num)
    if num < 2:
        print("Not prime")
    elif num == 2:
        print("Prime")
    elif num % 2 == 0:
        print("Not prime")
    else:
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")
else:
    print("Invalid input. Please enter a valid number.")