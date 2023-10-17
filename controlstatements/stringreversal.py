# Ask the end user to enter a string and then return the reversed string
'''
s = input("Enter a string: ")
print(s[::-1])
'''

s = input("Enter a string: ")
i = len(s) - 1
result = ''
while i >= 0:
    result = result + s[i]
    i = i-1
print(result)