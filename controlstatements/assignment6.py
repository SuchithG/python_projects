'''
Ask the user to enter a number and display that number 
skip the if the number is divisible by 10 
stop if number > 100
'''

n = int(input("Enter a number:"))
x = 0
while x < 100 and x < n:
    x += 1
    if x % 10 == 0:
        continue
    print(x)
    
