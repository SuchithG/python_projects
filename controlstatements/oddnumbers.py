# Display all the odd numbers from a range of numbers from min to max.
x = int(input("Enter the min value "))
y = int(input("Enter the max value "))

i=x
if i % 2 == 0:
    i= x+1
while i <= y:
    print(i)
    i+=2