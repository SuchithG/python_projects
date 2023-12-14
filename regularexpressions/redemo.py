import re 

str = "Take 1 up 14-12-2023 One 23 idea.One idea 45 at a time 21-12-2023"

result = re.search(r'o\w\w',str)
#print(result.group())

result = re.findall(r'o\w\w',str)
print(result)

result = re.match(r'T\w\w',str)
print(result.group())

result = re.sub(r'one','two',str)
print(result)

result = re.findall(r'o\w{1,2}',str)
print(result)

result = re.split(r'\d+',str)
print(result)

result = re.findall(r'O\w+',str) # print one or more characters, starting with the preceding alphabet
result = re.findall(r'O\w*',str) # Zero or more characters after O
result = re.findall(r'O\w?',str) # Zero or 1 after O
result = re.findall(r'O\w{1,2}',str) # specify the number of characters
print(result)

result = re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(result)

result = re.search(r'^T\w',str) # regular expression must be in the beginning of the string
print(result.group())

