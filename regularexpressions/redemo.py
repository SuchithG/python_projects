import re 

str = "Take 1 up One 23 idea.One idea 45 at a time"

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
print(result)

