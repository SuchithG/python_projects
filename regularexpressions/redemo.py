import re 

str = "Take up one idea.One idea at a time"
result = re.search(r'o\w\w',str)
print(result.group())