# Print from 1 to 20 , Skip multiples of 3
x=0

while x <= 20:
    x += 1
    if x % 3 == 0:
        continue
    print(x)