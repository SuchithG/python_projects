# single line strings
s = "you are awesome"
print(s)


# Multi-line strings
s1 = """You are the creator 
of you 
own destiny"""
print(s1)

print(s[4]) #Indexing

print(s*2) #Repetition

#Length function
print(len(s))
print(len(s1))

#Slicing
print(s[0:3]) # does not include the element in the ending index
print(s[0:])
print(s[:5])
print(s[-3:-1])

print(s[0:9:2]) # adding a step while indexing
print(s[10::-1])
print(s[::-1]) # starting index from the end

# Strip the spaces
u = " yes are sure "
print(u.strip()) # space removed at the beginning and end of the string
print(u.lstrip()) # space removed at the beginning of the string
print(u.rstrip()) # space removed at the right end of the string

# Location of a substring
print(u.find("re"),0,len(u)) # found a substring
print(u.count("2")) # number of occurrences
print(u.replace("yes","you")) # replace
print(u.upper()) # Upper case
print(u.lower()) # Lower case
print(u.title()) # every word will start with upper case