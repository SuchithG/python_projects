# Count the number of vowels in a given string or word

word = input('Enter a word: ')
vowels = {'a','e','i','o','u'}
result = {}

for c in word:
    if c in vowels:
        result[c] = result.get(c, 0) + 1
for k, v in result.items():
    print(k, " is present", v, " times")